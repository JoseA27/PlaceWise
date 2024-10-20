from abc import ABC, abstractmethod

# Clase Abstracta SocialMediaAdapter que define los metodos
class SocialMediaAdapter(ABC):
    _instances = {}

    # Metodo para garantizar Singleton
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SocialMediaAdapter, cls).__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    @abstractmethod
    def post(self, image_path, caption):
        pass
    @abstractmethod
    def get_posts(self, user_id):
        pass