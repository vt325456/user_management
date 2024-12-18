from minio import Minio
def minio_client():
    return Minio(
        "minio:9000",
        access_key="root",
        secret_key="root",
        secure=False
    )