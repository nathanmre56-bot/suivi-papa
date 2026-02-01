import streamlit as st
from datetime import datetime
import os

# 1. CONFIGURATION ET STYLE
st.set_page_config(page_title="Suivi Portfolio", layout="centered")

st.markdown("""
    <style>
    header, footer, #MainMenu {visibility: hidden;}
    .block-container {padding-top: 2rem;}
    .cadre-titre { border: 2px solid #1565C0; border-radius: 8px; padding: 10px; text-align: center; margin-bottom: 10px; margin-top: 15px; }
    .titre-texte { color: #1565C0; font-weight: bold; font-size: 16px; }
    .montant-style { text-align: center; font-size: 28px; font-weight: bold; color: #1976D2; margin-bottom: 20px; }
    .stButton { display: flex; justify-content: center; }
    .stButton > button { background-color: #1565C0 !important; color: white !important; font-weight: bold !important; border-radius: 10px !important; padding: 10px 30px !important; border: none !important; }
    input { text-align: center !important; font-size: 28px !important; font-weight: bold !important; color: #1976D2 !important; }
    div[data-baseweb="input"] { border: none !important; background-color: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GESTION DE LA MÉMOIRE ---
# On utilise la session pour éviter que ça saute pendant qu'il l'utilise
if 'montant' not in st.session_state:
    # On tente de lire le fichier, sinon on met la dernière valeur connue
    if os.path.exists("dernier_montant.txt"):
        with open("dernier_montant.txt", "r") as f:
            st.session_state.montant = float(f.read())
    else:
        st.session_state.montant = 59.57

# --- 3. CALCULS ---
date_depart = datetime(2026, 1, 1)
aujourdhui = datetime.now()
nb_mois = (aujourdhui.year - date_depart.year) * 12 + (aujourdhui.month - date_depart.month)
if aujourdhui.day < 2: nb_mois -= 1
investi = 63.85 + (nb_mois * 37) # Modifié à 37€ comme demandé

# --- 4. AFFICHAGE ---

# BLOC 1
st.markdown('<div class="cadre-titre"><div class="titre-texte">MONTANT INVESTI</div></div>', unsafe_allow_html=True)
st.markdown(f'<div class="montant-style">{investi:.2f} €</div>', unsafe_allow_html=True)

# BLOC 2
st.markdown('<div class="cadre-titre"><div class="titre-texte">MONTANT ACTUEL (€)</div></div>', unsafe_allow_html=True)

# L'input utilise la session state
actuel = st.number_input("Saisie", label_visibility="collapsed", value=st.session_state.montant, step=0.01)

if st.button("💾 ENREGISTRER"):
    st.session_state.montant = actuel
    with open("dernier_montant.txt", "w") as f:
        f.write(str(actuel))
    st.toast("✅ Montant sauvegardé !")

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
