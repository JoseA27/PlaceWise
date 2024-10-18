import boto3
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

class CognitoService:
    def __init__(self):
        self.client = boto3.client(
            'cognito-idp',
            region_name=settings.AWS_COGNITO_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        self.user_pool_id = settings.AWS_COGNITO_USER_POOL_ID

    def get_user(self, access_token):
        try:
            response = self.client.get_user(AccessToken=access_token)
            return response
        except self.client.exceptions.NotAuthorizedException:
            raise PermissionDenied("Invalid token or token expired")

    def check_permission(self, access_token, required_permission):
        user_info = self.get_user(access_token)
        username = user_info['Username']
        user = User.objects.get(username=username)

        if not user.has_perm(required_permission):
            raise PermissionDenied("User does not have the required permission")

        return True