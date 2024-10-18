import requests
from django.conf import settings
from .social_media_adapter import SocialMediaAdapter

class InstagramAdapter(SocialMediaAdapter):
    def post(self, image_path, caption):
        url = 'https://graph.facebook.com/v11.0/me/media'
        
        # Step 1: Upload the image
        image_data = {
            'image_url': image_path,  # Use a public URL for the image
            'caption': caption,
            'access_token': settings.INSTAGRAM_ACCESS_TOKEN,
        }
        
        media_response = requests.post(url, data=image_data)
        media_id = media_response.json().get('id')

        # Step 2: Publish the media
        publish_url = f'https://graph.facebook.com/v11.0/{media_id}/publish'
        publish_response = requests.post(publish_url, data={
            'access_token': settings.INSTAGRAM_ACCESS_TOKEN
        })

        return publish_response.json()
    
    def get_posts(self, user_id):
        url = f'https://graph.facebook.com/v11.0/{user_id}/media'
        params = {'access_token': settings.INSTAGRAM_ACCESS_TOKEN}
        response = requests.get(url, params=params)
        return response.json()