import base64
import logging
from sqlalchemy import select, update, func
import traceback
from uuid import UUID
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, HTTPException, Depends
from app.services.invitation_service import generate_qr_code
from app.database import Database
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.invitation_model import Invitation
from app.models.user_model import User
from settings.config import Settings

router = APIRouter()

@router.post("/send-invitation/")
async def send_invitation(inviter_id: UUID, invitee_email: str, db: AsyncSession = Depends(Database.get_session_factory)):
    try:
        
        invitation = await generate_qr_code(inviter_id, invitee_email, db)
        return {"message": "Invitation has been sent successfully!", "qr_code_url": invitation.qr_code_url}
    
    except HTTPException as httpexec:
        raise httpexec
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/redirect/")
async def redirect_invitation(inviter: str, db: AsyncSession = Depends(Database.get_session_factory)):
    """
    Redirect to redirect_url when QR code is scanned
    """
    try:
        decoded_nickname = base64.urlsafe_b64decode(inviter).decode()
        
        async with db() as session:
            result = await session.execute(
                select(Invitation).join(User).where(User.nickname == decoded_nickname)
            )
            invitation = result.scalars().first()
        
        if not invitation:
            raise HTTPException(status_code=404, detail="Invalid invitation or user not found.")
        
        async with db() as session:
            if invitation.status != "accepted":
                await session.execute(update(Invitation).where(Invitation.id == invitation.id).values(status="accepted"))
                await session.commit()
        
        redirect_url = Settings.Config.redirect_url
        return RedirectResponse(url=redirect_url)
    
    except Exception as e:
        logging.error(f"Failed during QR code redirect: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/invitation-count/")
async def get_invitation_count(user_id: UUID, db: AsyncSession = Depends(Database.get_session_factory)):
    try:
        async with db() as session:
            total_invites_query = await session.execute(select(func.count(Invitation.id)).filter(Invitation.inviter_id == user_id))
            total_invites = total_invites_query.scalar() or 0

            accepted_invites_query = await session.execute(select(func.count(Invitation.id)).filter(Invitation.inviter_id == user_id,Invitation.status == "accepted"))
            accepted_invites = accepted_invites_query.scalar() or 0
            
        acceptance_details = {"user_id": str(user_id),"total_invites_sent": total_invites,"total_invites_accepted": accepted_invites}

        return acceptance_details

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching stats: {str(e)}")