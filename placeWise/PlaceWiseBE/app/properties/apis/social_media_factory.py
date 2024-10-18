from .facebook_adapter import FacebookAdapter
from .twitter_adapter import TwitterAdapter
from .instagram_adapter import InstagramAdapter
from .tiktok_adapter import TikTokAdapter

class SocialMediaFactory:
    @staticmethod
    def get_adapter(social_media_type):
        if social_media_type == 'facebook':
            return FacebookAdapter()
        elif social_media_type == 'twitter':
            return TwitterAdapter()
        elif social_media_type == 'instagram':
            return InstagramAdapter()
        elif social_media_type == 'tiktok':
            return TikTokAdapter()
        else:
            raise ValueError("Unsupported social media type.")# 