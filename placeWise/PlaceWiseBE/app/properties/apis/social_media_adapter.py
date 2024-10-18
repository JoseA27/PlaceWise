from abc import ABC, abstractmethod

class SocialMediaAdapter(ABC):
    @abstractmethod
    def post(self, image_path, caption):
        pass