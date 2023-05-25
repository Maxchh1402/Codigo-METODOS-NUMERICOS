import numpy as np
import streamlit as st
import pandas as pd
import numpy as np

def cramer(A,b):
  n = len(b)
  D = np.linalg.det(A)
  x = np.zeros(n)
  c = 0
  lista_x = []
  lista_c = []
  for k in range(n):
    Ak = A.copy()
    Ak[:,k] = b
    Dk = np.linalg.det(Ak)
    x[k] = Dk/D
    c = c+1

    lista_x.append(round(x[k], 5))
    lista_c.append(c)
  
  cols = st.columns(3)
  currentCol = 0
  lenght = len(lista_x)

  st.subheader("Numero de soluciones: " + str(lenght))    

  for i in lista_x:
    cols[currentCol].metric('Xn', i)
    currentCol = (currentCol + 1) % len(cols)  
  
