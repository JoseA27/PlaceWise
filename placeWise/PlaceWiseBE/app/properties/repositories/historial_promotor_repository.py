from ..models.HistorialPromotor import HistorialPromotor

# Documentación
# Clase que representa el repositorio del historial del promotor
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos

class HistorialPromotorRepository:
    # Historial Promotor
    # Método que obtiene todo el historial de promotor
    @staticmethod
    def get_all_historial_promotor():
        return HistorialPromotor.objects.all()

    # Método que crea un historial de promotor
    # recibe los datos validados del historial de promotor
    @staticmethod
    def crear_historial_promotor(validated_data):
        try:
            historial = HistorialPromotor.objects.create(**validated_data)
            return historial
        except Exception as e:
            print(f"Error al crear el historial de promotor: {str(e)}")
            return None