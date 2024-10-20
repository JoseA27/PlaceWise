from ..models.SolicitudesPromotor import SolicitudPromotor
from ..models.PropiedadModel import Propiedad
from ..models.PropiedadesPorPromotor import PropiedadPorPromotor
from ..models.PromotorModel import Promotor
from ..models.MultimediaPorPropiedad import MultimediaPorPropiedad
from ..models.HistorialPromotor import HistorialPromotor

# Documentación
# Clase que representa el repositorio de propiedades
# Se encarga de realizar las operaciones de lectura y escritura en la base de datos


class PropertyRepository:
    # Solicitudes
    # Método que obtiene todas las solicitudes
    @staticmethod
    def get_all_solicitudes():
        return SolicitudPromotor.objects.all()

    # Método que crea una solicitud
    # recibe los datos validados de la solicitud
    @staticmethod
    def crear_solicitud(
        id_vendedor, id_comprador, id_propiedad, fecha_solicitud, status
    ):
        try:
            # Crear una nueva instancia del modelo SolicitudPromotor
            nueva_solicitud = SolicitudPromotor(
                idVendedor=id_vendedor,
                idComprador=id_comprador,
                idPropiedad=id_propiedad,
                fechaSolicitud=fecha_solicitud,
                status=status,
            )
            # Guardar en la base de datos
            nueva_solicitud.save()

            return nueva_solicitud
        except Exception as e:
            print(f"Error al guardar la solicitud: {str(e)}")
            return None

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

    # Propiedades por Promotor
    @staticmethod
    def get_all_propiedades_por_promotor():
        return PropiedadPorPromotor.objects.all()

    @staticmethod
    def crear_propiedad_por_promotor(validated_data):
        try:
            nueva_propiedad_por_promotor = PropiedadPorPromotor(**validated_data)
            nueva_propiedad_por_promotor.save()
            return nueva_propiedad_por_promotor
        except Exception as e:
            print(f"Error al guardar la propiedad por promotor: {str(e)}")
            return None

    # Multimedia por Propiedad
    @staticmethod
    def get_all_multimedia():
        return MultimediaPorPropiedad.objects.all()

    @staticmethod
    def crear_multimedia(validated_data):
        try:
            multimedia = MultimediaPorPropiedad.objects.create(**validated_data)
            return multimedia
        except Exception as e:
            print(f"Error al crear la multimedia: {str(e)}")
            return None

    # Historial Promotor
    @staticmethod
    def get_all_historial_promotor():
        return HistorialPromotor.objects.all()

    @staticmethod
    def crear_historial_promotor(validated_data):
        try:
            historial = HistorialPromotor.objects.create(**validated_data)
            return historial
        except Exception as e:
            print(f"Error al crear el historial de promotor: {str(e)}")
            return None
