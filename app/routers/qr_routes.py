from io import BytesIO
import logging
from pathlib import Path
import qrcode
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from app.utils.minio import minio_client
from app.dependencies import get_settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
settings = get_settings()

@router.get("/generate-and-store-qr/", tags=["minIO QR Invite"])
def generate_qr_code(data: str, fill_color: str = 'red', back_color: str = 'white', size: int = 10):
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
        qr = qrcode.QRCode(version=1, box_size=size, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img_byte_arr = BytesIO()
        img.save(img_byte_arr)
        img_byte_arr.seek(0)
        file_name = f"qr_codes/{data}.png"
        client = minio_client()
        bucket_name = "qrcodes-bucket"
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
        client.put_object(bucket_name, file_name, img_byte_arr, length=img_byte_arr.getbuffer().nbytes)
        logging.info(f"QR code successfully saved to Minio Bucket {bucket_name}")
        
        return f"QR code created! Added to Minio Bucket {bucket_name}"
        
    except Exception as e:
        logging.error(f"Failed to generate/save QR code: {e}")
        raise