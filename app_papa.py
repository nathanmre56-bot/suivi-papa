import streamlit as st
from datetime import datetime

# Configuration et masquage des menus
st.set_page_config(page_title="Suivi Portfolio", page_icon="📈")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    
    /* Supprimer les bordures grises par défaut de Streamlit autour de l'input */
    div[data-baseweb="input"] {
        border: none !important;
        background-color: transparent !important;
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

# --- AFFICHAGE ---

# 1. BLOC INVESTI
st.markdown(f"""
    <div style="border: 2px solid #1565C0; border-radius: 10px; padding: 15px; margin-bottom: 10px; text-align: center; background-color: white;">
        <div style="color: #1565C0; font-weight: bold; font-size: 14px; margin-bottom: 5px;">MONTANT INVESTI</div>
        <div style="color: #1976D2; font-weight: bold; font-size: 24px;">{investi:.2f} €</div>
    </div>
    """, unsafe_allow_html=True)

# 2. BLOC MONTANT ACTUEL (CORRIGÉ : Tout est dans le même div)
st.markdown('<div style="border: 2px solid #1565C0; border-radius: 10px; padding: 15px; margin-bottom: 10px; text-align: center; background-color: white;">', unsafe_allow_html=True)
st.markdown('<div style="color: #1565C0; font-weight: bold; font-size: 14px; margin-bottom: -15px;">MONTANT ACTUEL (€)</div>', unsafe_allow_html=True)

# Le widget de saisie
actuel = st.number_input("Saisie", label_visibility="collapsed", value=59.57, step=0.01)

st.markdown('</div>', unsafe_allow_html=True)

# 3. BLOC PERFORMANCE
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
