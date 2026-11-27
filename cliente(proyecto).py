# ============================================================
# Proyecto Final POO - Grupo 1: Alquiler de vehículos
# Integrantes:
#   - Integrante 1  Carrasco Proaño Hector Adrian
#   - Integrante 2  Lara Ruíz Valeria Lizbeth
#   - Integrante 3  Leon Alay Evelyn Maite
#   - Integrante 4  Ortiz Moran Anahí Valentina
# ============================================================

from vehiculo import Vehiculo
from auto import Auto


class Cliente:
    """Representa a la persona que alquila vehículos."""

    def __init__(self, cedula, nombre, telefono):
        self._cedula = cedula
        self._nombre = nombre
        self._telefono = ""
        self._alquileres = []  # historial: lista de (vehiculo, dias, costo)
        self.telefono = telefono  # usa el setter con validación


    @property
    def cedula(self):
        return self._cedula

    @property
    def nombre(self):
        return self._nombre


    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not valor.isdigit() or len(valor) != 10:
            raise ValueError("El teléfono debe tener 10 dígitos numéricos.")
        self._telefono = valor

    @property
    def alquileres(self):
        return list(self._alquileres)  # copia, protege el encapsulamiento


    def alquilar(self, vehiculo, dias):
        """Alquila un vehículo (cualquier subclase) y registra el costo."""
        vehiculo.marcar_alquilado()  # lanza error si no está disponible
        costo = vehiculo.calcular_costo(dias)  # polimorfismo
        self._alquileres.append((vehiculo, dias, costo))
        return costo

    def devolver(self, vehiculo):
        vehiculo.marcar_devuelto()

    def total_gastado(self):
        return sum(costo for _, _, costo in self._alquileres)

    def __str__(self):
        return (f"Cliente: {self._nombre} (C.I.: {self._cedula}) "
                f"- Tel: {self._telefono} - Alquileres: {len(self._alquileres)}")




if __name__ == "__main__":
    c = Cliente("0912345678", "Juan Pérez", "0987654321")
    a = Auto("GYE-1234", "Chevrolet", "Spark", 25, 5, "Manual")

    print("=== Prueba de la clase Cliente ===")
    print(c)

    print("\n--- Alquilar y devolver ---")
    costo = c.alquilar(a, 3)
    print(a)
    print("Costo del alquiler:", costo)
    c.devolver(a)
    print(a)
    print(c)
    print("Total gastado:", c.total_gastado())

    print("\n--- Validaciones ---")
    try:
        c.telefono = "123"
    except ValueError as e:
        print("Error esperado:", e)

    try:
        c.alquilar(a, 2)
        c.alquilar(a, 2)
    except ValueError as e:
        print("Error esperado:", e)