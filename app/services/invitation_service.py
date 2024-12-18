import base64
from io import BytesIO
import logging
from pathlib import Path
from uuid import UUID
from sqlalchemy import select
from app.models.user_model import User
import qrcode
from app.utils.minio import minio_client
from app.dependencies import get_settings
from app.database import Database
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from settings.config import Settings
from app.models.invitation_model import Invitation

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def generate_qr_code(inviter_id: UUID, invitee_email: str, db:AsyncSession = Depends(Database.get_session_factory), fill_color: str = 'red', back_color: str = 'white', size: int = 10):
    """
    Generates a QR code based on the provided data and saves it to a specified file path.
    Parameters:
    - data (str): The data to encode in the QR code.
    - path (Path): The filesystem path where the QR code image will be saved.
    - fill_color (str): Color of the QR code.
    - back_color (str): Background color of the QR code.
    - size (int): The size of each box in the QR code grid.
    """
    logging.debug("QR code generation started")
    try:
        #get the record with the userid who is sending invite
        async with db() as session:
            result = await session.execute(select(User).where(User.id == inviter_id))
            inviter = result.scalars().first()
        
        encoded_nickname = base64.urlsafe_b64encode(inviter.nickname.encode()).decode()
        print("------------------reached1")
        qr_code_url = f"{Settings.Config.redirect_url}/redirect/?inviter={encoded_nickname}"
        print("------------------reached2")
        qr = qrcode.QRCode(version=1, box_size=size, border=5)
        qr.add_data(qr_code_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        print("------------------reached3")
        img_byte_arr = BytesIO()
        img.save(img_byte_arr)
        img_byte_arr.seek(0)
        
        file_name = f"qr_codes/{inviter_id}.png"
        
        client = minio_client()
        bucket_name = "qrcodes-bucket"
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            
        client.put_object(bucket_name, file_name, img_byte_arr, length=img_byte_arr.getbuffer().nbytes)
        
        invitation = Invitation(
        inviter_id=inviter_id,
        invitee_email=invitee_email,
        qr_code_url=qr_code_url
        )
        async with db() as session:
            session.add(invitation)
            await session.commit()
            await session.refresh(invitation)
        logging.info(f"QR code created! Added to Minio Bucket {bucket_name}")
        return invitation
        
        
    except Exception as e:
        logging.error(f"Failed to generate/save QR code: {e}")
        raise