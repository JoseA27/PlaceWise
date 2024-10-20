from ..models.PromotorModel import Promotor

# Documentación
# Clase que representa el repositorio de promotores
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos

class PromotorRepository:
    # Promotores
    # Método que obtiene todos los promotores
    @staticmethod
    def get_all_promotores():
        return Promotor.objects.all()

    # Método que crea un promotor
    # recibe los datos validados del promotor
    @staticmethod
    def crear_promotor(validated_data):
        try:
            promotor = Promotor.objects.create(**validated_data)
            return promotor
        except Exception as e:
            print(f"Error al crear el promotor: {str(e)}")
            return None