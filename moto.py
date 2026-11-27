

# ============================================================
# Proyecto Final POO - Grupo 1: Alquiler de vehículos
# Integrantes:
#   - Integrante 1  Carrasco Proaño Hector Adrian
#   - Integrante 2  Lara Ruíz Raleria Lizbeth
#   - Integrante 3  Leon Alay Evelyn Maite
#   - Integrante 4  Ortiz Moran Anahí Valentina
# ============================================================

from vehiculo import Vehiculo


class Moto(Vehiculo):
    """
    Clase que representa una moto y hereda de Vehiculo.
    """

    def __init__(self, placa, marca, modelo, tarifa_diaria, cilindraje, incluye_casco):
        super().__init__(placa, marca, modelo, tarifa_diaria)
        self.__cilindraje = cilindraje
        self.__incluye_casco = incluye_casco

    @property
    def cilindraje(self):
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, nuevo_cilindraje):
        if nuevo_cilindraje <= 0:
            raise ValueError("Cilindraje no valido")
        self.__cilindraje = nuevo_cilindraje

    @property
    def incluye_casco(self):
        return self.__incluye_casco

    @incluye_casco.setter
    def incluye_casco(self, nuevo_casco):
        self.__incluye_casco = nuevo_casco

    def tipo(self):
        return "Moto"

    def requisitos(self):
        if self.__cilindraje > 250:
            return "Licencia tipo A y casco"
        return "Licencia y casco"

    def calcular_costo(self, dias):
        if dias <= 0:
            raise ValueError("Dias no validos")
        costo = self.tarifa_diaria * dias
        if self.__cilindraje > 250:
            costo = costo * 1.15
        if dias >= 5:
            costo = costo * 0.90
        return round(costo, 2)

    def __str__(self):
        return f"Moto [{self.__dict__.__str__()}]"


if __name__ == "__main__":
    m1 = Moto("GYE-101", "Yamaha", "FZ25", 22.0, 250, True)
    print(m1)
    print(f"Tipo: {m1.tipo()}")
    print(f"Requisitos: {m1.requisitos()}")
    print(f"Costo 3 dias: {m1.calcular_costo(3)}")

    m1.cilindraje = 300
    print(f"Nuevo cilindraje: {m1.cilindraje}")
    print(f"Requisitos: {m1.requisitos()}")
    print(f"Costo 5 dias: {m1.calcular_costo(5)}")
