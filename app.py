import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


disp_button = st.button('Construir grafico de dispersion')  # crear un botón
if disp_button:  # al hacer clic en el botón

    st.write(
        'Creación de un grafico de disperción para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.show()

# crear una casilla de verificación
# hist_button = st.button('Construir grafico de dispersion')  # crear un botón
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

# crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
# hist_button = st.button('Construir grafico de dispersion')  # crear un botón
build_disper = st.checkbox('Construir un grafico de dispersion')

if build_disper:  # si la casilla de verificación está seleccionada
    st.write('Construir un grafico de dispersion para la columna odómetro')

# crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    fig.show()
