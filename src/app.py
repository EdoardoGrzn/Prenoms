import streamlit as st
from query import prenoms, tous_prenoms

st.set_page_config(page_title="Prénoms en France", page_icon="📈", layout="centered")

@st.cache_data
def load_data():
    return tous_prenoms()

st.title("Evolution des prenoms francais")
liste_prenoms = load_data()

prenom = st.selectbox("Entrez le prenom", liste_prenoms, index = None)

if prenom : 
    df = prenoms(prenom)
    st.line_chart(df, x = "periode", y = "total")

st.markdown(
    """
    <style>
    .footer_right { position: fixed; right: 16px; bottom: 8px;
            font-size: 0.8rem; color: gray; }
    .footer_left { position: fixed; left: 16px; bottom: 8px;
            font-size: 0.8rem; color: gray; }
    .footer_middle { position: fixed; left: 50%; bottom: 8px; transform: translateX(-50%);
            font-size: 0.8rem; color: gray; }
    </style>
    <div class="footer_left">Données issues de l'INSEE</div>
    <div class="footer_middle"><a href="https://exemple.com" target="_blank">Plus d'informations</a></div>
    <div class="footer_right">Fait par Edoardo Graziano</div>
    """,
    unsafe_allow_html=True,
)