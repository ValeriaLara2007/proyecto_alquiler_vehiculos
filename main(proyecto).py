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
from moto import Moto
from bicicleta import Bicicleta
from cliente import Cliente
from alquiler import Alquiler


def titulo(texto):
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


# ------------------------------------------------------------
# 1. CREACIÓN DE OBJETOS
# ------------------------------------------------------------
titulo("1. CREACIÓN DE LA FLOTA DE VEHÍCULOS")

auto1 = Auto("GYE-1234", "Chevrolet", "Spark", 25, 5, "Manual")
auto2 = Auto("GYE-5678", "Kia", "Rio", 35, 4, "Automática")
moto1 = Moto("MOT-101", "Yamaha", "FZ25", 22.0, 250, True)
moto2 = Moto("MOT-202", "Honda", "CB500", 40.0, 500, True)
bici1 = Bicicleta("BIC-01", "Trek", "Marlin 5", 10, "montaña", es_electrica=False)
bici2 = Bicicleta("BIC-02", "Specialized", "Turbo", 15, "urbana", es_electrica=True)

# Lista con objetos de DISTINTAS subclases (base del polimorfismo)
flota = [auto1, auto2, moto1, moto2, bici1, bici2]

for v in flota:
    print(v)

# ------------------------------------------------------------
# 2. POLIMORFISMO: mismo método, comportamiento distinto
# ------------------------------------------------------------
titulo("2. POLIMORFISMO: tipo(), requisitos() y calcular_costo()")

for v in flota:
    print(f"\n{v.marca} {v.modelo}")
    print(f"  Tipo        : {v.tipo()}")
    print(f"  Requisitos  : {v.requisitos()}")
    print(f"  Costo 2 días: ${v.calcular_costo(2):.2f}")
    print(f"  Costo 5 días: ${v.calcular_costo(5):.2f}")

# ------------------------------------------------------------
# 3. CLIENTES
# ------------------------------------------------------------
titulo("3. CREACIÓN DE CLIENTES")

cliente1 = Cliente("0912345678", "Juan Pérez", "0987654321")
cliente2 = Cliente("0923456789", "María López", "0991234567")
print(cliente1)
print(cliente2)

# ------------------------------------------------------------
# 4. ALQUILERES CON LA CLASE Alquiler
# ------------------------------------------------------------
titulo("4. ALQUILERES (clase Alquiler)")

alq1 = Alquiler("ALQ-01", cliente1, auto1, 3)
alq2 = Alquiler("ALQ-02", cliente2, moto2, 5)
alq3 = Alquiler("ALQ-03", cliente1, bici2, 3)

alquileres = [alq1, alq2, alq3]
for alq in alquileres:
    alq.iniciar_alquiler()
    print(f"{alq.codigo} | {alq.cliente.nombre} | {alq.vehiculo.tipo()} "
          f"{alq.vehiculo.marca} | {alq.dias} día(s) | Total: ${alq.total:.2f} "
          f"| Activo: {alq.activo}")

# ------------------------------------------------------------
# 5. ALQUILER DIRECTO DESDE Cliente (historial)
# ------------------------------------------------------------
titulo("5. ALQUILER DIRECTO DESDE Cliente (historial y total gastado)")

costo = cliente2.alquilar(auto2, 4)
print(f"{cliente2.nombre} alquiló {auto2.marca} {auto2.modelo} por 4 días: ${costo:.2f}")
costo = cliente2.alquilar(bici1, 2)
print(f"{cliente2.nombre} alquiló {bici1.marca} {bici1.modelo} por 2 días: ${costo:.2f}")
print(cliente2)
print(f"Total gastado por {cliente2.nombre}: ${cliente2.total_gastado():.2f}")

# ------------------------------------------------------------
# 6. DISPONIBILIDAD
# ------------------------------------------------------------
titulo("6. DISPONIBILIDAD DE LA FLOTA")

for v in flota:
    print(v)

# ------------------------------------------------------------
# 7. VALIDACIONES (encapsulamiento y errores controlados)
# ------------------------------------------------------------
titulo("7. VALIDACIONES")

# Alquilar un vehículo que ya está alquilado
try:
    cliente1.alquilar(auto1, 1)
    print("[SIN ERROR] Alquilar un vehículo ya alquilado")
except ValueError as e:
    print("[OK] Alquilar un vehículo ya alquilado ->", e)

# Tarifa diaria negativa
try:
    moto1.tarifa_diaria = -10
    print("[SIN ERROR] Tarifa diaria negativa")
except ValueError as e:
    print("[OK] Tarifa diaria negativa ->", e)

# Número de puertas inválido
try:
    auto1.num_puertas = 7
    print("[SIN ERROR] Número de puertas inválido")
except ValueError as e:
    print("[OK] Número de puertas inválido ->", e)

# Cilindraje inválido
try:
    moto1.cilindraje = 0
    print("[SIN ERROR] Cilindraje inválido")
except ValueError as e:
    print("[OK] Cilindraje inválido ->", e)

# Tipo de bicicleta inválido
try:
    bici1.tipo_bicicleta = "BMX"
    print("[SIN ERROR] Tipo de bicicleta inválido")
except ValueError as e:
    print("[OK] Tipo de bicicleta inválido ->", e)

# Teléfono inválido
try:
    cliente1.telefono = "123"
    print("[SIN ERROR] Teléfono inválido")
except ValueError as e:
    print("[OK] Teléfono inválido ->", e)

# Días inválidos al calcular el costo
try:
    auto2.calcular_costo(0)
    print("[SIN ERROR] Días inválidos en el costo")
except ValueError as e:
    print("[OK] Días inválidos en el costo ->", e)

# Días inválidos en Alquiler
try:
    alq1.dias = -2
    print("[SIN ERROR] Días inválidos en Alquiler")
except ValueError as e:
    print("[OK] Días inválidos en Alquiler ->", e)

# ------------------------------------------------------------
# 8. DEVOLUCIONES
# ------------------------------------------------------------
titulo("8. DEVOLUCIONES")

for alq in alquileres:
    alq.finalizar_alquiler()
    print(f"{alq.codigo} finalizado | Activo: {alq.activo} | "
          f"Vehículo disponible: {alq.vehiculo.disponible}")

cliente2.devolver(auto2)
cliente2.devolver(bici1)

titulo("9. ESTADO FINAL DE LA FLOTA")
for v in flota:
    print(v)