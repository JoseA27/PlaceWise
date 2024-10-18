import requests
from django.conf import settings
from .social_media_adapter import SocialMediaAdapter

class TikTokAdapter(SocialMediaAdapter):
    def post(self, video_path, caption):
        url = 'https://open-api.tiktok.com/media/upload/'
        
        # Assuming video_path is a public URL or you handle the video upload to their servers
        video_data = {
            'video_url': video_path,  # Use a public URL for the video
            'caption': caption,
            'access_token': settings.TIKTOK_ACCESS_TOKEN,
        }
        
        response = requests.post(url, data=video_data)
        
        return response.json()
    def get_posts(self, user_id):
        url = f'https://open-api.tiktok.com/user/{user_id}/videos/'
        params = {'access_token': settings.TIKTOK_ACCESS_TOKEN}
        response = requests.get(url, params=params)
        return response.json()