import streamlit as st
import pandas as pd
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False) 

st.write("""
# Capturando datos del MINSAL.
Esto es *una prueba* usando streamlit para capturar datos con pandas de una página que tiene alguna tabla html y mostrarla. 
***



""")


def cargar_datos():
    url = "https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/"
    html = pd.read_html(url, header=1, decimal=",")
    df = html[0]
    df.rename(columns={'Unnamed: 0':'Regiones'}, inplace=True)
    return df

df = cargar_datos()


df.drop(df.tail(1).index,inplace=True) # drop last n rows

st.subheader( f"La cantidad de Filas es: {df.shape[0]} y columnas {df.shape[1]}" )

df

# # # quitamos los puntos poque piensa que es decimal
df['Casos confirmados acumulados'] = df['Casos confirmados acumulados'].str.replace('.', '', regex=True).astype(float)

# # # df[['Regiones','Casos confirmados acumulados']] pasar solo 2 columnas

sns.displot(df[['Regiones','Casos confirmados acumulados']],y='Regiones',x='Casos confirmados acumulados',color='#00BFC4')
st.pyplot()