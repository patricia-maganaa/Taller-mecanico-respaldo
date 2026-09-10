# La clase Vehiculo representa el molde (plantilla) base para crear objetos vehículo.
# Declaración de atributos con sus tipos.
class Vehiculo:
    patente: str
    anio: int
    _en_taller: bool

    # Constructor que inicializa una nueva instancia de la clase Vehiculo
    def __init__(self, patente, anio):
        # Asigna la patente del vehículo recibida por parámetro
        self.patente = patente
        # Asigna el año de fabricación del vehículo recibido por parámetro
        self.anio = anio
        # Inicializa siempre en False ya que un vehículo recién registrado no parte dentro del taller
        self._en_taller = False
