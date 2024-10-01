import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_costo(x):
    return 50 + 5 * x

presupuesto = 500

st.title('Maximización del Almacenamiento de Datos en la Nube')

st.write('Este programa maximiza la cantidad de datos almacenados (en TB) sin exceder el presupuesto de 500 dólares.')

x = st.slider('Seleccione la cantidad de almacenamiento en TB (1 ≤ x ≤ 100)', min_value=1, max_value=100, value=10)

costo = calcular_costo(x)

st.write(f'Almacenamiento seleccionado: {x} TB')
st.write(f'Costo total: {costo} dólares')

if costo > presupuesto:
    st.warning(f'Advertencia: El costo excede el presupuesto de {presupuesto} dólares.')

almacenamiento_x = np.arange(1, 101)
costo_y = [calcular_costo(i) for i in almacenamiento_x]

fig, ax = plt.subplots()

ax.plot(almacenamiento_x, costo_y, marker='o', linestyle='-', color='purple', label='Costo de Almacenamiento', linewidth=2)
ax.set_xlabel('Almacenamiento (TB)')
ax.set_ylabel('Costo (dólares)')
ax.axhline(presupuesto, color='red', linestyle='--', linewidth=1, label=f'Presupuesto: {presupuesto} dólares')

ax.grid(True)

ax.set_ylim(0, max(costo_y) + 50)
ax.set_xlim(1, 100)

for i, txt in enumerate(costo_y):
    if i % 10 == 0: 
        ax.text(almacenamiento_x[i], costo_y[i] + 10, f'{txt}', fontsize=8, ha='center')

ax.legend()

st.pyplot(fig)


