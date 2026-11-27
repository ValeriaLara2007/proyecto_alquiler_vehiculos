# ============================================================
# Proyecto Final POO - Grupo 1: Alquiler de vehículos
# Integrantes:
#   - Integrante 1  Carrasco Proaño Hector Adrian
#   - Integrante 2  Lara Ruíz Raleria Lizbeth
#   - Integrante 3  Leon Alay Evelyn Maite
#   - Integrante 4  Ortiz Moran Anahí Valentina
# ============================================================

from vehiculo import Vehiculo


class Bicicleta(Vehiculo):
    """Subclase que representa una bicicleta disponible para alquiler."""

    TIPOS_VALIDOS = ("montaña", "ruta", "urbana", "paseo")

    def __init__(self, placa, marca, modelo, tarifa_diaria, tipo_bicicleta, es_electrica=False):
        super().__init__(placa, marca, modelo, tarifa_diaria)
        self._tipo_bicicleta = None
        self._es_electrica = None

        self.tipo_bicicleta = tipo_bicicleta
        self.es_electrica = es_electrica

    # ---------- Getters / Setters ----------

    @property
    def tipo_bicicleta(self):
        return self._tipo_bicicleta

    @tipo_bicicleta.setter
    def tipo_bicicleta(self, valor):
        if not isinstance(valor, str) or valor.strip().lower() not in self.TIPOS_VALIDOS:
            raise ValueError(
                f"Tipo de bicicleta inválido. Opciones permitidas: {', '.join(self.TIPOS_VALIDOS)}."
            )
        self._tipo_bicicleta = valor.strip().lower()

    @property
    def es_electrica(self):
        return self._es_electrica

    @es_electrica.setter
    def es_electrica(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El atributo 'es_electrica' debe ser booleano (True o False).")
        self._es_electrica = valor

    # ---------- Métodos sobrescritos (Polimorfismo) ----------

    def tipo(self):
        modalidad = "Eléctrica" if self._es_electrica else "Convencional"
        return f"Bicicleta ({self._tipo_bicicleta.capitalize()}, {modalidad})"

    def calcular_costo(self, dias):
        """
        Calcula el costo total para bicicletas:
        - Si es eléctrica, suma un 25% sobre la tarifa diaria.
        - Si el alquiler es de 3 días o más, aplica un 10% de descuento.
        """
        if dias <= 0:
            raise ValueError("La cantidad de días debe ser mayor a 0.")

        tarifa_efectiva = self._tarifa_diaria * (1.25 if self._es_electrica else 1.0)
        total = tarifa_efectiva * dias

        if dias >= 3:
            total *= 0.90

        return round(total, 2)

    def requisitos(self):
        if self._es_electrica:
            return "Documento de identidad y uso obligatorio de casco"
        return "Uso de casco (no requiere licencia)"


# ---------- Ejecución de prueba de la clase Bicicleta ----------
if __name__ == "__main__":
    b1 = Bicicleta("BIC-01", "Trek", "Marlin 5", 10, "montaña", es_electrica=False)
    b2 = Bicicleta("BIC-02", "Specialized", "Turbo", 15, "urbana", es_electrica=True)

    print("=== Prueba de la clase Bicicleta ===")
    print(b1)
    print("Tipo:", b1.tipo())
    print("Requisitos:", b1.requisitos())
    print("Costo por 2 días:", b1.calcular_costo(2))

    print("\n--- Bicicleta eléctrica ---")
    print(b2)
    print("Tipo:", b2.tipo())
    print("Requisitos:", b2.requisitos())
    print("Costo por 3 días (con recargo + descuento):", b2.calcular_costo(3))

    print("\n--- Validaciones ---")
    try:
        b1.tipo_bicicleta = " BMX "
    except ValueError as e:
        print("Error esperado:", e)

    try:
        b1.es_electrica = "si"
    except ValueError as e:
        print("Error esperado:", e)