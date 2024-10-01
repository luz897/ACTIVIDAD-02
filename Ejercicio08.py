import streamlit as st
import matplotlib.pyplot as plt

def calcular_rendimiento(x):
    if x <= 10:
        return x 
    else:
        return x - 0.1 * (x - 10) 
def calcular_energia(x):
    return x * 10  

st.title('Maximización del Tamaño del Lote en Entrenamiento de Deep Learning')
st.write('Este programa calcula el tamaño de lote óptimo para maximizar el rendimiento bajo una restricción de consumo de energía.')

x = st.slider('Seleccione el tamaño del lote', min_value=1, max_value=20, value=10)

energia_consumida = calcular_energia(x)
rendimiento = calcular_rendimiento(x)

if energia_consumida > 200:
    st.write(f'Consumo de energía excedido: {energia_consumida} unidades. El tamaño del lote debe reducirse.')
else:
    st.write(f'Rendimiento para un lote de tamaño {x}: {rendimiento:.2f} unidades.')
    st.write(f'Consumo de energía: {energia_consumida} unidades.')

# Gráfico
fig, ax = plt.subplots()

lotes_x = list(range(1, 21))
rendimiento_y = [calcular_rendimiento(i) for i in lotes_x]

ax.plot(lotes_x, rendimiento_y, marker='o', linestyle='--', color='purple', linewidth=2, markersize=8, label='Rendimiento')

for i, txt in enumerate(rendimiento_y):
    ax.annotate(f'{txt:.2f}', (lotes_x[i], rendimiento_y[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black')

ax.set_xlabel('Tamaño del Lote', fontsize=12, color='black')
ax.set_ylabel('Rendimiento', fontsize=12, color='black')
ax.set_title('Rendimiento en función del tamaño del lote', fontsize=14, color='black')
ax.grid(True, linestyle='-.', linewidth=0.7)

ax.set_xlim(1, 20)
ax.set_ylim(0, max(rendimiento_y) + 5)
ax.legend()

st.pyplot(fig)
