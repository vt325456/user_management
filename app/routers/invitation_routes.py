from sqlalchemy import select
import traceback
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from app.services.invitation_service import generate_qr_code
from app.database import Database
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.invitation_model import Invitation

router = APIRouter()


@router.post("/send-invite/")
async def send_invitation(inviter_id: UUID, invitee_email: str, db: AsyncSession = Depends(Database.get_session_factory)):
    try:
        print("Inside send invite")
        invitation = await generate_qr_code(inviter_id, invitee_email, db)
        print(invitation)
        return {"message": "Invitation has been sent successfully!", "qr_code_url": invitation.qr_code_url}
    except HTTPException as httpexec:
        raise httpexec
    except Exception as e:
        print("Error Traceback:", traceback.format_exc())
        raise HTTPException(status_code=400, detail=str(e))