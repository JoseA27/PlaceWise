from django.conf import settings
import requests

class HubSpotService:
    def __init__(self):
        self.api_key = settings.HUBSPOT_API_KEY
        self.base_url = "https://api.hubapi.com"

    def create_post(self, content, platform):
        url = f"{self.base_url}/social/v1/posts"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "content": content,
            "platform": platform
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()

    def get_posts(self):
        url = f"{self.base_url}/social/v1/posts"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def delete_post(self, post_id):
        url = f"{self.base_url}/social/v1/posts/{post_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.delete(url, headers=headers)
        return response.status_code

    def monitor_post(self, post_id):
        url = f"{self.base_url}/social/v1/posts/{post_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        return response.json()