import math
import streamlit as st
import pandas as pd
import numpy as np


def biseccion():
    c = 0
    i = 1
    with st.form(key='calc_biseccion'):
        a = st.number_input('Valor de a: ', value= 3)
        b = st.number_input('Valor de b: ', value = 3.5)
        tol = st.number_input('Tolerancia: ', format="%.4f", step = 1e-4, value = 0.001 )
        n0 = st.number_input('Iteraciones: ', value = 100)
        calcular = st.form_submit_button('Calcular')
    
    fa = pow(a, 3) - (6 * pow(a, 2)) + (11*a) - 6.1
    fb = pow(b, 3) - (6 * pow(b, 2)) + (11*b) - 6.1
    pab = fa * fb

    lista_xn = []
    lista_e = []
    lista_c = []
    lista_a = []
    lista_b = []
 

    xn=0
    e = 0
    
    if pab < 0:
        while i < n0:

            x = (a + b) / 2
            fx = pow(x, 3) - (6 * pow(x, 2)) + (11 * x) - 6.1
            pax = fa * fx
            
            if pax < 0:
                b = x
            else:
                a = x
            xn = (a + b) / 2
            c = c + 1
            e = abs(xn - x) / xn
            x = xn
            i = i + 1

            lista_xn.append(xn)
            lista_e.append(e)
            lista_c.append(c)
            lista_a.append(a)
            lista_b.append(b)


            if e < tol:
               
                st.write("\nProcedure completed successfully\n")
                break

    else:
        st.write ("No hay raiz")
    
    d = {'a':lista_a, 'b':lista_b, 'Xn':lista_xn, 'e':lista_e }
    df = pd.DataFrame(data=d, index = lista_c )
    st.table(df)

    st.subheader("iteraciones: " + str(c))
    st.subheader("Raiz es igual a: " + str(xn))
    st.subheader("Error: " + str(e))
