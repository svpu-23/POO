# ==============================================
# PREDICCIÓN DE VENTAS COCA-COLA - FUNCIÓN EXPONENCIAL
# ==============================================

import math
import matplotlib.pyplot as plt  # Para visualizar las ventas

# --------------------------
# Datos base
# --------------------------
V0 = 100      # Ventas del primer mes (miles de cajas)
a = 1.05      # Crecimiento estimado (5% mensual)

# Función exponencial
def ventas_exponenciales(t):
    return V0 * (a ** t)

# --------------------------
# Uso del modelo
# --------------------------

print("\n💡 Predicción de ventas Coca-Cola (Modelo Exponencial)")

# Mostrar ventas proyectadas por varios meses
meses = list(range(1, 13))  # 12 meses
ventas_proyectadas = [ventas_exponenciales(m) for m in meses]

for i, v in zip(meses, ventas_proyectadas):
    print(f"Mes {i}: {v:.2f} mil cajas")

# Predicción personalizada
mes_input = int(input("\n¿Para qué mes deseas predecir ventas? → "))
print(f"\n📈 Predicción estimada para el mes {mes_input}: {ventas_exponenciales(mes_input):.2f} mil cajas\n")

# --------------------------
# Gráfico visual
# --------------------------
plt.plot(meses, ventas_proyectadas, marker='o')
plt.title('Proyección de Ventas Coca-Cola con Función Exponencial')
plt.xlabel('Mes')
plt.ylabel('Miles de Cajas')
plt.grid(True)
plt.show()
