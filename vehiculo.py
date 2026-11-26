
# ============================================================
# Proyecto Final POO - Grupo 1: Alquiler de vehículos
# Integrantes:
#   - Integrante 1  Carrasco Proaño Hector Adrian
#   - Integrante 2  Lara Ruíz Raleria Lizbeth
#   - Integrante 3  Leon Alay Evelyn Maite
#   - Integrante 4  Ortiz Moran Anahí Valentina
# ============================================================

class Vehiculo:
    """Clase base: representa cualquier vehículo disponible para alquiler."""

    def __init__(self, placa, marca, modelo, tarifa_diaria):
        self._placa = placa
        self._marca = marca
        self._modelo = modelo
        self._tarifa_diaria = 0
        self._disponible = True
        self.tarifa_diaria = tarifa_diaria  # usa el setter con validación

    # ---------- Getters / Setters ----------
    @property
    def placa(self):
        return self._placa

    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def tarifa_diaria(self):
        return self._tarifa_diaria

    @tarifa_diaria.setter
    def tarifa_diaria(self, valor):
        if valor <= 0:
            raise ValueError("La tarifa diaria debe ser mayor a 0.")
        self._tarifa_diaria = valor

    @property
    def disponible(self):
        return self._disponible

    # ---------- Métodos ----------
    def marcar_alquilado(self):
        if not self._disponible:
            raise ValueError(f"El vehículo {self._placa} no está disponible.")
        self._disponible = False

    def marcar_devuelto(self):
        self._disponible = True

    def tipo(self):
        return "Vehículo"

    def calcular_costo(self, dias):
        """Método que será sobrescrito (polimorfismo) en cada subclase."""
        return self._tarifa_diaria * dias

    def requisitos(self):
        """Método que será sobrescrito (polimorfismo) en cada subclase."""
        return "Ninguno"

    def __str__(self):
        estado = "Disponible" if self._disponible else "Alquilado"
        return (f"[{self.tipo()}] {self._marca} {self._modelo} "
                f"(Placa: {self._placa}) - ${self._tarifa_diaria:.2f}/día - {estado}")

# ---------- Ejecución de prueba de la clase Vehiculo ----------
if __name__ == "__main__":
    v = Vehiculo("XXX-000", "Genérica", "Base", 20)

    print("=== Prueba de la clase Vehiculo ===")
    print(v)
    print("Tipo:", v.tipo())
    print("Requisitos:", v.requisitos())
    print("Costo por 3 días:", v.calcular_costo(3))

    print("\n--- Alquilar y devolver ---")
    v.marcar_alquilado()
    print(v)
    v.marcar_devuelto()
    print(v)

    print("\n--- Validaciones ---")
    try:
        v.tarifa_diaria = -5
    except ValueError as e:
        print("Error esperado:", e)

    try:
        v.marcar_alquilado()
        v.marcar_alquilado()
    except ValueError as e:
        print("Error esperado:", e)