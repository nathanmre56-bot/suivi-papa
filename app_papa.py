import streamlit as st
from datetime import datetime

# 1. STYLE DES CADRES POUR LES TITRES
st.set_page_config(page_title="Suivi Portfolio", layout="centered")

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    
    /* Le cadre autour des titres uniquement */
    .cadre-titre {
        border: 2px solid #1565C0;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        margin-bottom: 10px;
        margin-top: 15px;
    }
    
    .titre-texte {
        color: #1565C0;
        font-weight: bold;
        font-size: 16px;
    }

    /* Style des montants sous les cadres */
    .montant-style {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #1976D2;
        margin-bottom: 20px;
    }

    /* Aligner le montant saisi */
    input {
        text-align: center !important;
        font-size: 28px !important;
        font-weight: bold !important;
        color: #1976D2 !important;
    }
    div[data-baseweb="input"] {
        border: none !important;
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CALCULS ---
date_depart = datetime(2026, 1, 1)
aujourdhui = datetime.now()
nb_mois = (aujourdhui.year - date_depart.year) * 12 + (aujourdhui.month - date_depart.month)
if aujourdhui.day < 2: nb_mois -= 1
investi = 63.85 + (nb_mois * 35)

# --- 3. AFFICHAGE ---

# PARTIE 1
st.markdown('<div class="cadre-titre"><div class="titre-texte">MONTANT INVESTI</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="montant-style">{investi:.2f} €</div>', unsafe_allow_html=True)

# PARTIE 2
st.markdown('<div class="cadre-titre"><div class="titre-texte">MONTANT ACTUEL (€)</div></div>', unsafe_allow_html=True)
actuel = st.number_input("Saisie", label_visibility="collapsed", value=59.57, step=0.01)

# PARTIE 3
st.markdown('<div class="cadre-titre"><div class="titre-texte">PERFORMANCE</div></div>', unsafe_allow_html=True)
diff = actuel - investi
pourcent = (diff / investi) * 100 if investi != 0 else 0
couleur_perf = "green" if diff >= 0 else "red"
signe = "+" if diff >= 0 else ""

st.markdown(f"""
    <div style="text-align: center; font-weight: bold; margin-top: 10px;">
        <div style="color: {couleur_perf}; font-size: 28px;">{signe}{pourcent:.2f} %</div>
        <div style="color: {couleur_perf}; font-size: 22px;">{signe}{diff:.2f} €</div>
    </div>
""", unsafe_allow_html=True)
