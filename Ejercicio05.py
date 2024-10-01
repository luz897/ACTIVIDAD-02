import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def tiempo_entrenamiento(x):
    return 1000 / x + 0.1 * x

st.title("Minimización del Tiempo de Entrenamiento en Función del Batch Size")
st.write(r'La función de tiempo de entrenamiento es $T(x) = \frac{1000}{x} + 0.1x$')
st.write("El tamaño del batch debe estar entre 16 y 128.")

limites = (16, 128)

resultado = minimize(lambda x: tiempo_entrenamiento(x[0]), x0=[64], bounds=[limites])

st.write(f"El tamaño de batch que minimiza el tiempo de entrenamiento es: {resultado.x[0]:.2f}")

x_vals = np.linspace(16, 128, 500)
y_vals = tiempo_entrenamiento(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='T(x)', color='purple')
plt.axvline(resultado.x[0], color='red', linestyle='--', label=f'Batch size óptimo: {resultado.x[0]:.2f}')
plt.xlabel('Batch Size (x)')
plt.ylabel('Tiempo de Entrenamiento (T)')
plt.title('Minimización del Tiempo de Entrenamiento')
plt.legend()
plt.grid()

st.pyplot(plt)
