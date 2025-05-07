# -*- coding: utf-8 -*-

# ------------------------------
# MODELO DE RENDIMIENTO 100 MARIPOSA PERSONALIZADO
# ------------------------------
# Requiere: Spyder, pandas y matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# 1. DATOS PERSONALES Y DE TIEMPOS
# ------------------------------
altura = 1.66  # en metros
peso = 53      # en kg
edad = 33      # años

# Tiempos reales (en segundos)
tiempo_50 = 45.82
tiempo_100 = 111.65

# Parciales del 100m
parcial_50_1 = 49.23
parcial_50_2 = tiempo_100 - parcial_50_1

# ------------------------------
# 2. ANÁLISIS DE RITMO Y FATIGA
# ------------------------------
diferencia = parcial_50_2 - parcial_50_1
print(f"\nDiferencia entre parciales: {diferencia:.2f} segundos")
if diferencia > 2:
    print("👉 Estás perdiendo bastante en el segundo 50. Hay que trabajar la resistencia específica.")
elif diferencia > 1:
    print("⚠️ Hay fatiga moderada. Mejora técnica o ritmo podría ayudarte.")
else:
    print("✅ Buena distribución de ritmo.")

# ------------------------------
# 3. SIMULACIÓN DE MEJORA
# ------------------------------
# ¿Qué pasa si bajas 1 segundo el segundo 50?
simulacion_tiempo_100 = parcial_50_1 + (parcial_50_2 - 1)
print(f"\n🔧 Simulación con 1s menos en segundo 50: {simulacion_tiempo_100:.2f} s")

# ------------------------------
# 4. VISUALIZACIÓN DE PARCIALES
# ------------------------------
plt.figure()
plt.title("Parciales del 100 Mariposa")
plt.bar(['1er 50m', '2º 50m'], [parcial_50_1, parcial_50_2], color=['skyblue', 'salmon'])
plt.ylabel('Tiempo (s)')
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.show()

# ------------------------------
# 5. CÁLCULO DE VELOCIDAD Y EFICIENCIA
# ------------------------------
velocidad_total = 100 / tiempo_100  # m/s
velocidad_1 = 50 / parcial_50_1
velocidad_2 = 50 / parcial_50_2

print(f"\nVelocidad media total: {velocidad_total:.2f} m/s")
print(f"Velocidad 1er 50m: {velocidad_1:.2f} m/s")
print(f"Velocidad 2º 50m: {velocidad_2:.2f} m/s")

# ------------------------------
# 6. ANÁLISIS RESPIRATORIO PERSONALIZADO
# ------------------------------
print("\n--- Análisis de patrón respiratorio ---")

# Patrón respiratorio (estimado)
respiraciones_0_25 = 0  # Subacuático + 5 ciclos sin respirar
respiraciones_25_50 = 7  # Cada brazada (~6-8)
respiraciones_50_75 = 8  # Fatiga aumenta la frecuencia
respiraciones_75_100 = 9  # Variable, tiende a ser cada brazada

total_respiraciones = respiraciones_0_25 + respiraciones_25_50 + respiraciones_50_75 + respiraciones_75_100

print(f"Respiraciones por tramo:")
print(f"0-25m: {respiraciones_0_25}")
print(f"25-50m: {respiraciones_25_50}")
print(f"50-75m: {respiraciones_50_75}")
print(f"75-100m: {respiraciones_75_100}")
print(f"Total aproximado: {total_respiraciones} respiraciones")

# Recomendación simple
if respiraciones_75_100 >= 9:
    print("🔁 Recomendación: intenta alternar entre cada 1 y cada 2 brazadas, y entrena tramos sin respirar para mantener ritmo.")
else:
    print("✅ Buen control respiratorio en tramo final.")

# ------------------------------
# 7. EFICIENCIA POR BRAZADAS (PENDIENTE DE DATOS)
# ------------------------------
# Descomentar y rellenar cuando tengas los datos
# brazadas_0_25 = ...
# brazadas_25_50 = ...
# brazadas_50_75 = ...
# brazadas_75_100 = ...
#
# total_brazadas = brazadas_0_25 + brazadas_25_50 + brazadas_50_75 + brazadas_75_100
# eficiencia_total = tiempo_100 / total_brazadas
# print(f"\nTotal de brazadas: {total_brazadas}")
# print(f"Eficiencia media: {eficiencia_total:.2f} s por brazada")
# print(f"Longitud media por brazada: {100 / total_brazadas:.2f} metros")
