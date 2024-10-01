import streamlit as st
import matplotlib.pyplot as plt

def calcular_peticiones(nodos, x):
    return min(nodos * x, 400)  # No puede exceder las 400 peticiones por segundo

st.title('Maximización de Peticiones Procesadas por un Sistema Distribuido')
st.write('Este programa calcula la cantidad máxima de peticiones procesadas por un sistema distribuido de nodos.')

nodos = st.slider('Seleccione el número de nodos (máx. 20)', min_value=1, max_value=20, value=10)
x = st.slider('Seleccione el número de peticiones por segundo que procesa cada nodo (máx. 20)', min_value=1, max_value=20, value=20)

peticiones_procesadas = calcular_peticiones(nodos, x)
st.write(f'Cantidad de peticiones procesadas: {peticiones_procesadas:.2f} peticiones por segundo')

fig, ax = plt.subplots()

nodos_x = list(range(1, 21))  
peticiones_y = [calcular_peticiones(i, x) for i in nodos_x]  

ax.plot(nodos_x, peticiones_y, marker='o', linestyle='--', color='purple', linewidth=2, markersize=8, label='Peticiones Procesadas')

for i, txt in enumerate(peticiones_y):
    ax.annotate(f'{txt:.2f}', (nodos_x[i], peticiones_y[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='black')

ax.set_xlabel('Número de Nodos', fontsize=12, color='black')
ax.set_ylabel('Peticiones Procesadas', fontsize=12, color='black')
ax.set_title('Peticiones Procesadas en función del número de nodos', fontsize=14, color='black')
ax.grid(True, linestyle='-.', linewidth=0.7)

ax.set_xlim(1, 20)
ax.set_ylim(0, max(peticiones_y) + 50)
ax.legend()

st.pyplot(fig)



