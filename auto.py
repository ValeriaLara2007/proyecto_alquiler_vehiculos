
# ============================================================
# Proyecto Final POO - Grupo 1: Alquiler de vehículos
# Integrantes:
#   - Integrante 1  Carrasco Proaño Hector Adrian
#   - Integrante 2  Lara Ruíz Valeria Lizbeth
#   - Integrante 3  Leon Alay Evelyn Maite
#   - Integrante 4  Ortiz Moran Anahí Valentina
# ============================================================

from vehiculo import Vehiculo


class Auto(Vehiculo):
    """Subclase de Vehiculo: representa un automóvil disponible para alquiler."""

    SEGURO_DIARIO = 5  # costo fijo del seguro por día

    def __init__(self, placa, marca, modelo, tarifa_diaria,
                 num_puertas=4, transmision="Manual"):
        super().__init__(placa, marca, modelo, tarifa_diaria)
        self._num_puertas = 0
        self._transmision = transmision
        self.num_puertas = num_puertas  # usa el setter con validación


    @property
    def num_puertas(self):
        return self._num_puertas

    @num_puertas.setter
    def num_puertas(self, valor):

        if valor not in (2, 3, 4, 5):
            raise ValueError("El número de puertas debe ser 2, 3, 4 o 5.")
        self._num_puertas = valor

    @property
    def transmision(self):
        return self._transmision


    def tipo(self):
        return "Auto"

    def calcular_costo(self, dias):
        """Tarifa diaria + seguro obligatorio por cada día."""
        if dias <= 0:
            raise ValueError("Los días de alquiler deben ser mayores a 0.")
        return (self._tarifa_diaria + Auto.SEGURO_DIARIO) * dias

    def requisitos(self):
        return "Licencia tipo B vigente y cédula de identidad."

    def __str__(self):
        return (f"{super().__str__()} | {self._num_puertas} puertas, "
                f"transmisión {self._transmision}")



if __name__ == "__main__":
    a = Auto("GYE-1234", "Chevrolet", "Spark", 25, 5, "Manual")

    print("=== Prueba de la clase Auto ===")
    print(a)

    print("Tipo:", a.tipo())
    print("Requisitos:", a.requisitos())
    print("Costo por 3 días:", a.calcular_costo(3))

    print("\n--- Alquilar y devolver ---")
    a.marcar_alquilado()
    print(a)
    a.marcar_devuelto()
    print(a)

    print("\n--- Validaciones ---")
    try:
        a.num_puertas = 7
    except ValueError as e:
        print("Error esperado:", e)

    try:
        a.calcular_costo(0)
    except ValueError as e:
        print("Error esperado:", e)