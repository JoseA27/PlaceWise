from ..models.PropiedadesPorPromotor import PropiedadPorPromotor

# Documentación
# Clase que representa el repositorio de propiedades por promotor
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos

class PropiedadPorPromotorRepository:
    # Propiedades por Promotor
    # Método que obtiene todas las propiedades por promotor
    @staticmethod
    def get_all_propiedades_por_promotor():
        return PropiedadPorPromotor.objects.all()

    # Método que crea una propiedad por promotor
    # recibe los datos validados de la propiedad por promotor
    @staticmethod
    def crear_propiedad_por_promotor(validated_data):
        try:
            nueva_propiedad_por_promotor = PropiedadPorPromotor(**validated_data)
            nueva_propiedad_por_promotor.save()
            return nueva_propiedad_por_promotor
        except Exception as e:
            print(f"Error al guardar la propiedad por promotor: {str(e)}")
            return None