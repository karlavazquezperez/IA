import streamlit as st
import pandas as pd
import numpy as np                  # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt     # Para la generación de gráficas a partir de los datos
from apyori import apriori

header=st.container()
dataset=st.container()
elige_algoritmo=st.container()
resul=st.container()

with header:
	st.title('Familia de datos')
	st.text('Creado por Karla Vázquez Pérez')

with elige_algoritmo:
	st.header('Algoritmos')
	st.text('Aqui puedes elegir el algoritmo a implementar')

with dataset:
	st.header('Sube tu archivo')
	st.text('Carga tu archivo Excel (.csv) en el formato correcto')
	datos=pd.read_csv('movies.csv')
	st.write(datos)
	#Se incluyen todas las transacciones en una sola lista
	Transacciones = datos.values.reshape(-1).tolist() #-1 significa 'dimensión no conocida'
	#Se crea una matriz (dataframe) usando la lista y se incluye una columna 'Frecuencia'
	ListaM = pd.DataFrame(Transacciones)
	ListaM['Frecuencia'] = 1
	#Se agrupa los elementos
	ListaM = ListaM.groupby(by=[0], as_index=False).count().sort_values(by=['Frecuencia'], ascending=True) #Conteo
	ListaM['Porcentaje'] = (ListaM['Frecuencia'] / ListaM['Frecuencia'].sum()) #Porcentaje
	ListaM = ListaM.rename(columns={0 : 'Item'})
	# Se genera un gráfico de barras
	plt.figure(figsize=(16,20), dpi=300)
	plt.ylabel('Item')
	plt.xlabel('Frecuencia')
	plt.barh(ListaM['Item'], width=ListaM['Frecuencia'], color='pink')
	st.pyplot()

with resul:
	st.header('Resultados')
	st.text('Algoritmo implementado con tus datos')