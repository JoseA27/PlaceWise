from ..models.PropiedadModel import Propiedad

# Documentación
# Clase que representa el repositorio de propiedades
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos

class PropertyRepository:
    # Propiedades
    # Método que obtiene todas las propiedades
    @staticmethod
    def get_all_propiedades():
        return Propiedad.objects.all()

    # metodo que crea una propiedad
    # recibe los datos validados de la propiedad
    @staticmethod
    def crear_propiedad(validated_data):
        try:
            propiedad = Propiedad.objects.create(**validated_data)
            return propiedad
        except Exception as e:
            print(f"Error al crear la propiedad: {str(e)}")
            return None
