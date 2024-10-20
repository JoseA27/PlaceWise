from ..models.MultimediaPorPropiedad import MultimediaPorPropiedad

# Documentación
# Clase que representa el repositorio de multimedia por propiedad
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos

class MultimediaRepository:
    # Multimedia por Propiedad
    # Método que obtiene todas las multimedia
    @staticmethod
    def get_all_multimedia():
        return MultimediaPorPropiedad.objects.all()

    # Método que crea una multimedia
    # recibe los datos validados de la multimedia
    @staticmethod
    def crear_multimedia(validated_data):
        try:
            multimedia = MultimediaPorPropiedad.objects.create(**validated_data)
            return multimedia
        except Exception as e:
            print(f"Error al crear la multimedia: {str(e)}")
            return None