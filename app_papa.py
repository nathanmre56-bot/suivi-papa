import streamlit as st
from datetime import datetime
import os

# 1. CONFIGURATION ET STYLE
st.set_page_config(page_title="Suivi Portfolio", layout="centered")

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    .cadre-titre {
        border: 2px solid #1565C0;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        margin-bottom: 10px;
        margin-top: 15px;
    }
    .titre-texte { color: #1565C0; font-weight: bold; font-size: 16px; }
    .montant-style { text-align: center; font-size: 28px; font-weight: bold; color: #1976D2; margin-bottom: 20px; }
    input { text-align: center !important; font-size: 28px !important; font-weight: bold !important; color: #1976D2 !important; }
    div[data-baseweb="input"] { border: none !important; background-color: transparent !important; }
    
    /* Style pour le bouton centré */
    div.stButton > button {
        display: block;
        margin: 0 auto;
        background-color: #1565C0;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GESTION DE LA SAUVEGARDE ---
FICHIER_DATA = "dernier_montant.txt"

def charger_montant():
    if os.path.exists(FICHIER_DATA):
        try:
            with open(FICHIER_DATA, "r") as f:
                return float(f.read())
        except:
            return 59.57
    return 59.57

def sauver_montant(valeur):
    with open(FICHIER_DATA, "w") as f:
        f.write(str(valeur))

# --- 3. CALCULS ---
date_depart = datetime(2026, 1, 1)
aujourdhui = datetime.now()
nb_mois = (aujourdhui.year - date_depart.year) * 12 + (aujourdhui.month - date_depart.month)
if aujourdhui.day < 2: nb_mois -= 1
investi = 63.85 + (nb_mois * 35)

# --- 4. AFFICHAGE ---

# BLOC 1
st.markdown('<div class="cadre-titre"><div class="titre-texte">MONTANT INVESTI</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="montant-style">{investi:.2f} €</div>', unsafe_allow_html=True)

# BLOC 2
st.markdown('<div class="cadre-titre"><div class="titre-texte">MONTANT ACTUEL (€)</div></div>', unsafe_allow_html=True)
montant_charge = charger_montant()
actuel = st.number_input("Saisie", label_visibility="collapsed", value=montant_charge, step=0.01)

# BOUTON CENTRÉ
# On crée 3 colonnes, le bouton est dans celle du milieu pour le centrage visuel
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("💾 ENREGISTRER"):
        sauver_montant(actuel)
        st.toast("✅ Montant sauvegardé !") # Un petit message discret en bas

# BLOC 3
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
