from minio import Minio
def minio_client():
    return Minio(
        "minio:9000",
        access_key="rootuser",
        secret_key="rootpassword",
        secure=False
    )