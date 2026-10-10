import streamlit as st
from query import prenoms, tous_prenoms

st.cache_data
st.title("Evolution des prenoms francais")
liste_prenoms = tous_prenoms()

prenom = st.selectbox("Entrez le prenom", liste_prenoms, index = None  )

if prenom : 
    df = prenoms(prenom)
    st.line_chart(df, x = "periode", y = "total")