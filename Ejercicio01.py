import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

memoria_total = 1024

def calcular_datos_procesados(lotes, x):
    if lotes <= 5:
        return lotes * x
    else:
        
        return 5 * x + (lotes - 5) * 0.8 * x

st.title('Maximización de Datos Procesados por Lotes')

st.write('Este programa maximiza la cantidad de datos procesados considerando que a partir del lote 6 la eficiencia cae un 20%.')

lotes = st.slider('Seleccione el número de lotes (1 a 8)', min_value=1, max_value=8, value=5)

x = memoria_total / lotes

datos_procesados = calcular_datos_procesados(lotes, x)

st.write(f'Número de lotes: {lotes}')
st.write(f'Tamaño de cada lote: {x:.2f} MB')
st.write(f'Datos procesados: {datos_procesados:.2f} MB')

lotes_x = np.arange(1, 9)
datos_y = [calcular_datos_procesados(lote, memoria_total / lote) for lote in lotes_x]

fig, ax = plt.subplots()
ax.plot(lotes_x, datos_y, marker='o', linestyle='-', color='purple', label='Datos procesados')

for i, txt in enumerate(datos_y):
    ax.annotate(f'{txt:.2f}', (lotes_x[i], datos_y[i]), textcoords="offset points", xytext=(0,10), ha='center')

ax.set_xlabel('Número de lotes')
ax.set_ylabel('Datos procesados (MB)')
ax.set_title('Cantidad de datos procesados vs Número de lotes')
ax.grid(True)
ax.legend()

st.pyplot(fig)
