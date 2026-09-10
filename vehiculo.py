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

    # Getter para obtener la patente
    def obtener_patente(self):
        return self.__patente

    # Getter para obtener el año
    def obtener_anio(self):
        return self.__anio

    # Consulta si el vehículo se encuentra en el taller
    def esta_en_taller(self):
        return self.__en_taller


