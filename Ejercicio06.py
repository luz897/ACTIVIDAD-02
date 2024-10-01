import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Maximización de Archivos Transmitidos")

ancho_banda_total = 1000  
max_archivos = 50
reduction_start = 30
reduction_factor = 0.05

x = st.number_input("Ancho de banda utilizado por cada archivo (Mbps)", min_value=1, max_value=100, value=20)

def calcular_archivos_maximos(x):
    for n_archivos in range(1, max_archivos + 1):
        if n_archivos <= reduction_start:
            ancho_banda_utilizado = n_archivos * x
        else:
            ancho_banda_utilizado = n_archivos * x * (1 - reduction_factor)
        
        if ancho_banda_utilizado > ancho_banda_total:
            return n_archivos - 1 

    return max_archivos

max_archivos_transmitidos = calcular_archivos_maximos(x)

st.write(f"El número máximo de archivos que se pueden transmitir es: {max_archivos_transmitidos}")

n_archivos_range = np.arange(1, max_archivos + 1)
ancho_banda_utilizado = []

for n_archivos in n_archivos_range:
    if n_archivos <= reduction_start:
        ancho_banda_utilizado.append(n_archivos * x)
    else:
        ancho_banda_utilizado.append(n_archivos * x * (1 - reduction_factor))

plt.figure(figsize=(8, 5))
plt.plot(n_archivos_range, ancho_banda_utilizado, label='Ancho de banda utilizado', color='purple')
plt.axhline(ancho_banda_total, color='red', linestyle='--', label='Ancho de banda total (1000 Mbps)')
plt.xlabel('Número de archivos transmitidos')
plt.ylabel('Ancho de banda utilizado (Mbps)')
plt.title('Uso del Ancho de Banda en Función del Número de Archivos')
plt.legend()
plt.grid()

st.pyplot(plt)

