import streamlit as st
from queries import prenoms, tous_prenoms, annee_dispo, prenoms_par_annee

st.set_page_config(page_title="Prénoms en France by Edoardo", page_icon="📈", layout="centered")
tab1, tab2 = st.tabs(["Evolution d'un prénom", "Top 50 des prénoms par année"])

with tab1 : 
    @st.cache_data
    def load_data():
        return tous_prenoms()

    st.title("Evolution des prenoms francais")
    liste_prenoms = load_data()

    prenom = st.selectbox("Entrez le prenom", liste_prenoms, index = None)

    if prenom : 
        df = prenoms(prenom)
        st.line_chart(df, x = "periode", y = "total")

with tab2 : 
    @st.cache_data
    def load_top_prenoms(annee):
        return prenoms_par_annee(annee)

    st.title("Top 50 des prénoms par année")
    debut, fin = annee_dispo()
    annee = st.slider("Année", debut, fin, 2000)
    df_top = load_top_prenoms(annee)

    st.bar_chart(df_top, x ="prenom", y ="total", x_label="Prénoms", y_label="Nombre de naissance", horizontal=True, sort="-total")


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