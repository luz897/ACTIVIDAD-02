import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def uso_cpu(x):
    return 2 * x**2 + 10 * x

def resolver_ecuacion(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        raiz_discriminante = np.sqrt(discriminante)
        x1 = (-b + raiz_discriminante) / (2*a)
        x2 = (-b - raiz_discriminante) / (2*a)
        return x1, x2
    else:
        return None, None

st.title('Minimización del Uso de CPU en un Servidor Web')
st.write('Este programa calcula el número de peticiones por segundo que minimiza el uso de CPU sin exceder el 80% de capacidad.')

x = st.slider('Seleccione el número de peticiones por segundo (mín. 10)', min_value=10, max_value=20, value=10)

uso = uso_cpu(x)
st.write(f'Uso de CPU: {uso:.2f}%')

x1, x2 = resolver_ecuacion(2, 10, -80)
st.write(f'Los valores de x que cumplen con la restricción de CPU son: {x1:.2f} y {x2:.2f}')

fig, ax = plt.subplots()

datos_x = np.linspace(10, 20, 100)
cpu_y = [uso_cpu(i) for i in datos_x]

ax.plot(datos_x, cpu_y, marker='o', linestyle='--', color='purple', linewidth=2, markersize=4, label='Uso de CPU')

ax.set_xlabel('Peticiones por Segundo', fontsize=12, color='black')
ax.set_ylabel('Uso de CPU (%)', fontsize=12, color='black')
ax.set_title('Uso de CPU en función de las Peticiones por Segundo', fontsize=14, color='black')
ax.grid(True, linestyle='-.', linewidth=0.7)

ax.set_xlim(10, 20)
ax.set_ylim(0, max(cpu_y) + 10)
ax.legend()

st.pyplot(fig)
