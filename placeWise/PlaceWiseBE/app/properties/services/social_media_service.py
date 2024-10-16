from apis import SocialMediaFactory

class SocialMediaService:
    def __init__(self):
        self.factory = SocialMediaFactory()

    def post_to_social_media(self, platform, content, media_path):
        adapter = self.factory.get_adapter(platform.lower())
        if not adapter:
            raise ValueError(f"Unsupported social media platform: {platform}")

        # Determinar el tipo de contenido y llamar al método adecuado
        return adapter.post(media_path, content)

    def get_user_posts(self, platform, user_id):
        adapter = self.factory.get_adapter(platform.lower())
        if not adapter:
            raise ValueError(f"Unsupported social media platform: {platform}")

        return adapter.get_posts(user_id) 