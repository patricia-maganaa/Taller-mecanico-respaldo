# La clase Vehiculo representa el molde (plantilla) base para crear objetos vehículo.
# Declaración de atributos con sus tipos.
class Vehiculo:
    __patente: str
    __anio: int
    __en_taller: bool

    # Constructor que inicializa una nueva instancia de la clase Vehiculo
    def __init__(self, patente, anio):
        # Atributo privado encapsulado con doble guión bajo
        self.__patente = patente
        # Atributo privado encapsulado con doble guión bajo
        self.__anio = anio
        # Inicializa siempre en False ya que un vehículo recién registrado no parte dentro del taller
        self.__en_taller = False

    # Método para ingresar el vehículo al taller
    def ingresar(self):
        self.__en_taller = True

    # Método para entregar el vehículo (sale del taller)
    def entregar(self):
        self.__en_taller = False

    @property
    def patente(self):
        return self.__patente

    @property
    def anio(self):
        return self.__anio

    @property
    def en_taller(self):
        return self.__en_taller

    # Métodos alternativos por compatibilidad
    def obtener_patente(self):
        return self.patente

    def obtener_anio(self):
        return self.anio

    def esta_en_taller(self):
        return self.en_taller


