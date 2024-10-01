import streamlit as st
import matplotlib.pyplot as plt

def tiempo_ejecucion(x):
    return 5 * x + 2

st.title('Maximización de Datos Procesados por el Script')
st.write('Este programa calcula el número máximo de datos que puede procesar el script sin exceder los 50 segundos.')

x = st.slider('Seleccione el número de datos (máx. 9)', min_value=1, max_value=9, value=5)

tiempo = tiempo_ejecucion(x)
st.write(f'Tiempo de ejecución: {tiempo:.2f} segundos')

fig, ax = plt.subplots()

datos_x = list(range(1, 10))
tiempo_y = [tiempo_ejecucion(i) for i in datos_x]

ax.plot(datos_x, tiempo_y, marker='o', linestyle='--', color='purple', linewidth=2, markersize=8, label='Tiempo de Ejecución')

for i, txt in enumerate(tiempo_y):
    ax.annotate(f'{txt:.2f}', (datos_x[i], tiempo_y[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black')

ax.set_xlabel('Número de Datos', fontsize=12, color='black')
ax.set_ylabel('Tiempo de Ejecución (segundos)', fontsize=12, color='black')
ax.set_title('Tiempo de Ejecución en función del número de datos', fontsize=14, color='black')
ax.grid(True, linestyle='-.', linewidth=0.7)

ax.set_xlim(1, 9)
ax.set_ylim(0, max(tiempo_y) + 10)
ax.legend()

st.pyplot(fig)
