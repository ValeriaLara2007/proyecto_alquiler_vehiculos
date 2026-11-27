

# ============================================================
# Proyecto Final POO - Grupo 1: Alquiler de vehículos
# Integrantes:
#   - Integrante 1  Carrasco Proaño Hector Adrian
#   - Integrante 2  Lara Ruíz Raleria Lizbeth
#   - Integrante 3  Leon Alay Evelyn Maite
#   - Integrante 4  Ortiz Moran Anahí Valentina
# ============================================================


class Alquiler:
    """
    Clase que representa el alquiler de un vehiculo a un cliente.
    """

    def __init__(self, codigo, cliente, vehiculo, dias):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__vehiculo = vehiculo
        self.__dias = dias
        self.__total = 0.0
        self.__activo = False

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def vehiculo(self):
        return self.__vehiculo

    @property
    def dias(self):
        return self.__dias

    @dias.setter
    def dias(self, nuevos_dias):
        if nuevos_dias <= 0:
            raise ValueError("Dias no validos")
        self.__dias = nuevos_dias

    @property
    def total(self):
        return self.__total

    @property
    def activo(self):
        return self.__activo

    def calcular_total(self):
        self.__total = round(self.__vehiculo.calcular_costo(self.__dias), 2)
        return self.__total

    def iniciar_alquiler(self):
        self.__vehiculo.marcar_alquilado()
        self.calcular_total()
        self.__activo = True

    def finalizar_alquiler(self):
        self.__vehiculo.marcar_devuelto()
        self.__activo = False

    def __str__(self):
        return f"Alquiler [{self.__dict__.__str__()}]"


if __name__ == "__main__":
    from moto import Moto

    class ClientePrueba:
        def __init__(self, nombre):
            self.__nombre = nombre

        @property
        def nombre(self):
            return self.__nombre

    c1 = ClientePrueba("Carlos Mendoza")
    m1 = Moto("GYE-101", "Yamaha", "FZ25", 22.0, 250, True)

    alq1 = Alquiler("ALQ-01", c1, m1, 3)
    alq1.iniciar_alquiler()
    print(alq1)
    print(f"Total a pagar: {alq1.total}")

    alq1.finalizar_alquiler()
    print(alq1)
