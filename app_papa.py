import streamlit as st
from datetime import datetime

# 1. NETTOYAGE TOTAL DE L'INTERFACE STREAMLIT
st.set_page_config(page_title="Suivi Portfolio", layout="centered")

st.markdown("""
    <style>
    /* Supprimer les bordures et fonds par défaut de Streamlit */
    [data-testid="stAppViewContainer"], [data-testid="stVerticalBlock"] {
        background-color: white !important;
        border: none !important;
    }
    /* Cacher le menu et le header */
    header, footer {visibility: hidden;}
    
    /* Style de nos cadres personnalisés */
    .cadre-bleu {
        border: 2px solid #1565C0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        text-align: center;
        background-color: white;
    }
    .titre-cadre {
        color: #1565C0;
        font-weight: bold;
        font-size: 14px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }
    /* Forcer le champ de saisie à être invisible visuellement */
    div[data-baseweb="input"] {
        background-color: transparent !important;
        border: none !important;
    }
    input {
        text-align: center !important;
        font-size: 28px !important;
        font-weight: bold !important;
        color: #1976D2 !important;
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

# BLOC 1 : INVESTI
st.markdown(f'<div class="cadre-bleu"><div class="titre-cadre">Montant Investi</div><div style="color: #1976D2; font-size: 28px; font-weight: bold;">{investi:.2f} €</div></div>', unsafe_allow_html=True)

# BLOC 2 : ACTUEL (SAISIE)
st.markdown('<div class="cadre-bleu"><div class="titre-cadre">Montant Actuel (€)</div>', unsafe_allow_html=True)
actuel = st.number_input("Saisie", label_visibility="collapsed", value=59.57, step=0.1)
st.markdown('</div>', unsafe_allow_html=True)

# BLOC 3 : PERFORMANCE
diff = actuel - investi
pourcent = (diff / investi) * 100 if investi != 0 else 0
couleur_perf = "green" if diff >= 0 else "red"
sign
