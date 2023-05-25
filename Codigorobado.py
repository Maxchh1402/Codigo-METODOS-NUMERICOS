import streamlit as st
import numpy as np
import pandas as pd
#___________________________________
import biseccion as bs
import newton as nw
import secante as sc
import regulafalsi as fp
import cramer as cr
from PIL import Image

st.title ("Métodos Numéricos")
image = Image.open('metodos.jpg')
st.image(image)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Tercer Evaluacion Parcial")
with col2:
    st.subheader("Erick López - 348916")


seleccion = st.selectbox("Seleccione una opción: ", ["Método Biseccion", "Método Newton", "Método Secante", "Método Falsa Posicion", "Método Cramer"])

if seleccion == "Método Biseccion": 
    st.subheader("Método de Bisección")
    st.latex('''x^3 - 6x^2 + 11x -6.1''')
    bs.biseccion()

if seleccion == "Método Newton": 
    st.subheader("Método de Newton-Raphson")
    col1, col2 = st.columns(2)
    with col1:
        st.latex('''x^3 - 6x^2 + 11x -6.1''')
    
    with col2:
        st.latex('''\dfrac {\mathrm{d}}{\mathrm{d} x}= 3x^2-12x+11''')
    nw.newton()

if seleccion == "Método Secante": 
    st.subheader("Método de Secante")
    st.latex('''x^3 - 6x^2 + 11x -6.1''')
    sc.secante()

if seleccion == "Método Falsa Posicion": 
    st.subheader("Método de Falsa Posicion")
    st.latex('''x^3 - 6x^2 + 11x -6.1''')
    fp.regulafalsi()

if seleccion == "Método Cramer": 
    st.subheader("Método de Cramer")
    with col1:
        st.latex('''x + y = 1''')
    with col2:
        st.latex('''x + 5y = 10''')
        
    A = np.array([ [1,1], [1,5]])
    b = np.array([1,10])

    cr.cramer(A,b)
    
    image = Image.open('ratoncito.jfif')
    st.image(image, width = 400, caption = "Gracias por su atención")
