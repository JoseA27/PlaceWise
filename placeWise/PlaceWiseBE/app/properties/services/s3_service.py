import boto3
from django.conf import settings
from botocore.exceptions import NoCredentialsError

class S3Service:
    def __init__(self):
        
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )

    def upload_file(self, file, bucket_name, object_name=None):
        if object_name is None:
            object_name = file.name

        try:
            self.s3_client.upload_fileobj(file, bucket_name, object_name)
            return f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        except NoCredentialsError:
            return "Credentials not available"
