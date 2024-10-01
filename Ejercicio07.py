import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def tiempo_respuesta(x):
    return (100 / x) + 2 * x

st.title("Minimización del Tiempo de Respuesta en un Sistema de Colas")
st.write("Este programa calcula el tiempo de respuesta para diferentes tasas de procesamiento.")

x = st.slider("Selecciona la tasa de procesamiento (trabajos por segundo):", min_value=5, max_value=20, value=5)

T_x = tiempo_respuesta(x)
st.write(f"El tiempo de respuesta para {x} trabajos por segundo es: {T_x:.2f} segundos.")

fig, ax = plt.subplots()

datos_x = np.linspace(5, 20, 100)
tiempo_y = [tiempo_respuesta(i) for i in datos_x]

ax.plot(datos_x, tiempo_y, marker='o', linestyle='--', color='purple', linewidth=2, markersize=4, label='Tiempo de Respuesta')

ax.set_xlabel('Tasa de Procesamiento (trabajos por segundo)', fontsize=12, color='black')
ax.set_ylabel('Tiempo de Respuesta (segundos)', fontsize=12, color='black')
ax.set_title('Tiempo de Respuesta en Función de la Tasa de Procesamiento', fontsize=14, color='black')
ax.grid(True, linestyle='-.', linewidth=0.7)


ax.set_xlim(5, 20)
ax.set_ylim(0, max(tiempo_y) + 10)
ax.legend()

st.pyplot(fig)
