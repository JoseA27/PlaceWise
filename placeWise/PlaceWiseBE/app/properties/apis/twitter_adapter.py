import requests
from django.conf import settings
from .social_media_adapter import SocialMediaAdapter

class TwitterAdapter(SocialMediaAdapter):
    def post(self, image_path, tweet):
        url = 'https://upload.twitter.com/1.1/media/upload.json'
        files = {'media': open(image_path, 'rb')}
        media_response = requests.post(url, files=files, auth=settings.TWITTER_ACCESS_TOKEN)
        media_id = media_response.json().get('media_id_string')

        tweet_url = 'https://api.twitter.com/1.1/statuses/update.json'
        tweet_data = {
            'status': tweet,
            'media_ids': media_id
        }
        tweet_response = requests.post(tweet_url, data=tweet_data, auth=settings.TWITTER_ACCESS_TOKEN)
        return tweet_response.json()
    def get_posts(self, user_id):
        url = f'https://api.twitter.com/2/users/{user_id}/tweets'
        headers = {'Authorization': f'Bearer {settings.TWITTER_BEARER_TOKEN}'}
        response = requests.get(url, headers=headers)
        return response.json()