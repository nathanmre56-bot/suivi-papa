import streamlit as st
from datetime import datetime

# Masquer les menus Streamlit
st.set_page_config(page_title="Suivi Portfolio", page_icon="📈")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem;}
    /* Style pour masquer le fond gris du widget de saisie */
    div[data-baseweb="input"] {
        background-color: transparent !important;
        border: none !important;
    }
    input {
        text-align: center !important;
        font-weight: bold !important;
        color: #1976D2 !important;
        font-size: 24px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CALCULS ---
date_depart = datetime(2026, 1, 1)
aujourdhui = datetime.now()
nb_mois = (aujourdhui.year - date_depart.year) * 12 + (aujourdhui.month - date_depart.month)
if aujourdhui.day < 2: nb_mois -= 1
investi = 63.85 + (nb_mois * 35)

# --- DESIGN DES BLOCS ---
def debut_bloc(titre):
    st.markdown(f"""
    <div style="border: 2px solid #1565C0; border-radius: 10px; padding: 10px; margin-bottom: 5px; text-align: center; background-color: white;">
        <div style="color: #1565C0; font-weight: bold; font-size: 14px; margin-bottom: 2px;">{titre}</div>
    """, unsafe_allow_html=True)

def fin_bloc():
    st.markdown("</div>", unsafe_allow_html=True)

# --- AFFICHAGE ---

# 1. Bloc Investi
debut_bloc("MONTANT INVESTI")
st.markdown(f"<div style='color: #1976D2; font-weight: bold; font-size: 24px;'>{investi:.2f} €</div>", unsafe_allow_html=True)
fin_bloc()

# 2. Bloc Montant Actuel (ENCADRÉ)
debut_bloc("MONTANT ACTUEL (€)")
# On place le widget de saisie à l'intérieur du cadre
actuel = st.number_input("Saisie", label_visibility="collapsed", value=59.57, step=0.1)
fin_bloc()

# 3. Bloc Performance
diff = actuel - investi
pourcent = (diff / investi) * 100 if investi != 0 else 0
couleur_perf = "green" if diff >= 0 else "red"
signe = "+" if diff >= 0 else ""

debut_bloc("PERFORMANCE")
st.markdown(f"""
    <div style="color: {couleur_perf}; font-weight: bold; font-size: 24px;">{signe}{pourcent:.2f} %</div>
    <div style="color: {couleur_perf}; font-weight: bold; font-size: 20px;">{signe}{diff:.2f} €</div>
""", unsafe_allow_html=True)
fin_bloc()
