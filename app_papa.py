import streamlit as st
from datetime import datetime

# 1. CONFIGURATION ET FORCE DU DESIGN
st.set_page_config(page_title="Suivi Portfolio", layout="centered")

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    
    /* Le cadre bleu unique pour chaque section */
    .cadre-unique {
        border: 2px solid #1565C0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        text-align: center;
        background-color: white;
    }
    
    .titre-bleu {
        color: #1565C0;
        font-weight: bold;
        font-size: 14px;
        text-transform: uppercase;
        margin-bottom: 5px;
    }

    /* Force la zone de saisie Streamlit à devenir invisible et à remonter */
    div[data-baseweb="input"] {
        background-color: transparent !important;
        border: none !important;
        margin-top: -15px !important; /* Aspire le montant dans le cadre */
    }
    
    input {
        text-align: center !important;
        font-size: 28px !important;
        font-weight: bold !important;
        color: #1976D2 !important;
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

# BLOC 1 : INVESTI
st.markdown(f"""
    <div class="cadre-unique">
        <div class="titre-bleu">Montant Investi</div>
        <div style="color: #1976D2; font-size: 28px; font-weight: bold;">{investi:.2f} €</div>
    </div>
""", unsafe_allow_html=True)

# BLOC 2 : ACTUEL (SAISIE DANS LE CADRE)
st.markdown('<div class="cadre-unique"><div class="titre-bleu">Montant Actuel (€)</div>', unsafe_allow_html=True)
# La saisie est placée ici, le CSS 'margin-top' la fera remonter dans le div ci-dessus
actuel = st.number_input("Saisie", label_visibility="collapsed", value=59.57, step=0.01)
st.markdown('</div>', unsafe_allow_html=True)

# BLOC 3 : PERFORMANCE
diff = actuel - investi
pourcent = (diff / investi) * 100 if investi != 0 else 0
couleur_perf = "green" if diff >= 0 else "red"
signe = "+" if diff >= 0 else ""

st.markdown(f"""
    <div class="cadre-unique">
        <div class="titre-bleu">Performance</div>
        <div style="color: {couleur_perf}; font-size: 28px; font-weight: bold;">{signe}{pourcent:.2f} %</div>
        <div style="color: {couleur_perf}; font-size: 22px; font-weight: bold;">{signe}{diff:.2f} €</div>
    </div>
""", unsafe_allow_html=True)
