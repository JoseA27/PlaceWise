import requests
from django.conf import settings
from .social_media_adapter import SocialMediaAdapter

# Adaptador para la API de Facebook
class FacebookAdapter(SocialMediaAdapter):
    def post(self, image_path, caption):
        url = f'https://graph.facebook.com/v11.0/me/photos'
        files = {'file': open(image_path, 'rb')}
        data = {
            'caption': caption,
            'access_token': settings.FACEBOOK_ACCESS_TOKEN
        }
        response = requests.post(url, files=files, data=data)
        return response.json()
    def get_posts(self, user_id):
        url = f'https://graph.facebook.com/v11.0/{user_id}/posts'
        params = {'access_token': settings.FACEBOOK_ACCESS_TOKEN}
        response = requests.get(url, params=params)
        return response.json()