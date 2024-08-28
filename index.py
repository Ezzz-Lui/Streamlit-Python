import streamlit as st
import random
import pandas as pd

# Título de la app
st.title("Juego de Probabilidad y Estadística")

# Explicación inicial
st.write("""
Este es un simple juego de probabilidad utilizando un dado. 
Puedes lanzar el dado y ver el resultado, además de explorar estadísticas básicas.
""")

# Botón para lanzar el dado
if st.button("Lanzar Dado"):
    resultado = random.randint(1, 6)
    st.write(f"El dado muestra: {resultado}")
else:
    st.write("Haz clic en 'Lanzar Dado' para comenzar.")

# Simulación de múltiples lanzamientos
st.write("## Simulación de múltiples lanzamientos")
num_lanzamientos = st.slider("Selecciona el número de lanzamientos", 10, 1000, 100)

lanzamientos = [random.randint(1, 6) for _ in range(num_lanzamientos)]
conteo = pd.Series(lanzamientos).value_counts().sort_index()

st.bar_chart(conteo)

# Estadísticas básicas
st.write("## Estadísticas Básicas")

st.write(f"Número total de lanzamientos: {num_lanzamientos}")
st.write(f"Frecuencia de cada cara del dado:")
st.write(conteo)

# Probabilidades teóricas
st.write("## Probabilidades Teóricas")
st.write("""
Cada cara del dado tiene una probabilidad teórica de 1/6 (~16.67%). 
A medida que aumentes el número de lanzamientos, las frecuencias observadas deberían acercarse a estos valores.
""")

# Gráfico de barras con probabilidades teóricas y observadas
prob_teorica = pd.Series([1/6]*6, index=[1, 2, 3, 4, 5, 6])
prob_observada = conteo / num_lanzamientos

comparacion = pd.DataFrame({
    "Probabilidad Teórica": prob_teorica,
    "Probabilidad Observada": prob_observada
})

st.bar_chart(comparacion)

# Cierre
st.write("""
¡Explora la diferencia entre la probabilidad teórica y la observada, y prueba con diferentes números de lanzamientos!
""")
