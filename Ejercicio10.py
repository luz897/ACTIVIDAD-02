import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def calcular_latencia(x):
    return 100 - 2 * x

limite_latencia = 20

st.title('Maximización del Número de Mensajes en un Sistema de Mensajería')

st.write('Este programa maximiza el número de mensajes enviados sin que la latencia caiga por debajo de 20 ms.')

x = st.slider('Seleccione el número de mensajes por segundo (1 ≤ x ≤ 50)', min_value=1, max_value=50, value=10)

latencia = calcular_latencia(x)

st.write(f'Número de mensajes por segundo: {x}')
st.write(f'Latencia: {latencia} ms')

if latencia < limite_latencia:
    st.warning(f'Advertencia: La latencia ha caído por debajo del límite de {limite_latencia} ms.')

mensajes_x = np.arange(1, 51)
latencia_y = [calcular_latencia(i) for i in mensajes_x]

fig, ax = plt.subplots()

ax.plot(mensajes_x, latencia_y, marker='o', linestyle='-', color='purple', label='Latencia (ms)', linewidth=2)
ax.set_xlabel('Número de Mensajes por Segundo')
ax.set_ylabel('Latencia (ms)')
ax.axhline(limite_latencia, color='red', linestyle='--', linewidth=1, label=f'Límite de {limite_latencia} ms')

ax.set_ylim(0, max(latencia_y) + 10)
ax.set_xlim(1, 50)
ax.grid(True)

for i, txt in enumerate(latencia_y):
    if i % 5 == 0: 
        ax.text(mensajes_x[i], latencia_y[i] + 1, f'{txt}', fontsize=8, ha='center')

ax.legend()

st.pyplot(fig)

