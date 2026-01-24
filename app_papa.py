import streamlit as st
from datetime import datetime

# Masquer les menus Streamlit
st.set_page_config(page_title="Suivi Portfolio", page_icon="📈")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    /* Centrer le texte dans le champ de saisie */
    input {text-align: center !important;}
    </style>
    """, unsafe_allow_html=True)

# --- CALCULS ---
date_depart = datetime(2026, 1, 1)
aujourdhui = datetime.now()
nb_mois = (aujourdhui.year - date_depart.year) * 12 + (aujourdhui.month - date_depart.month)
if aujourdhui.day < 2: nb_mois -= 1
investi = 63.85 + (nb_mois * 35)

# --- DESIGN DES BLOCS ---
def creer_bloc(titre, valeur, couleur_texte="#1976D2"):
    st.markdown(f"""
    <div style="border: 2px solid #1565C0; border-radius: 10px; padding: 15px; margin-bottom: 10px; text-align: center; background-color: white;">
        <div style="color: #1565C0; font-weight: bold; font-size: 14px; margin-bottom: 5px;">{titre}</div>
        <div style="color: {couleur_texte}; font-weight: bold; font-size: 24px;">{valeur}</div>
    </div>
    """, unsafe_allow_html=True)

# --- AFFICHAGE ---

# Bloc 1 : Investi (Déjà ok)
creer_bloc("MONTANT INVESTI", f"{investi:.2f} €")

# Bloc 2 : Saisie avec CADRE
# On ouvre le div du cadre manuellement pour mettre le widget dedans
st.markdown("""
    <div style="border: 2px solid #1565C0; border-radius: 10px; padding: 15px; margin-bottom: 10px; text-align: center; background-color: white;">
        <div style="color: #1565C0; font-weight: bold; font-size: 14px; margin-bottom: 5px;">MONTANT ACTUEL (€)</div>
    """, unsafe_allow_html=True)

actuel = st.number_input("Label caché", label_visibility="collapsed", value=59.57, step=0.01)

st.markdown("</div>", unsafe_allow_html=True)

# Bloc 3 : Performance (Déjà ok)
diff = actuel - investi
pourcent = (diff / investi) * 100 if investi != 0 else 0
couleur_perf = "green" if diff >= 0 else "red"
signe = "+" if diff >= 0 else ""

st.markdown(f"""
<div style="border: 2px solid #1565C0; border-radius: 10px; padding: 15px; text-align: center; background-color: white;">
    <div style="color: #1565C0; font-weight: bold; font-size: 14px; margin-bottom: 5px;">PERFORMANCE</div>
    <div style="color: {couleur_perf}; font-weight: bold; font-size: 24px;">{signe}{pourcent:.2f} %</div>
    <div style="color: {couleur_perf}; font-weight: bold; font-size: 20px;">{signe}{diff:.2f} €</div>
</div>
""", unsafe_allow_html=True)
