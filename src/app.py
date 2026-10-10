import streamlit
from query import prenoms, tous_prenoms

st.cache_data
st.title("Evolution des prenoms francais")
prenoms = tous_prenoms()

prenom = st.selectbox("Entrez le prenom", prenoms, index = None  )

if prenom : 
    df = prenoms(prenom)
    st.line_chart(df, x = periode, y = valeur)