import streamlit as st
from datetime import datetime

# Configuration de la page
st.set_page_config(page_title="Suivi Investissement", page_icon="📈")

st.markdown("<h2 style='text-align: center; color: #1976D2;'>MON SUIVI 2026</h2>", unsafe_allow_html=True)

# --- CALCULS ---
date_depart = datetime(2026, 1, 1)
aujourdhui = datetime.now()
nb_mois = (aujourdhui.year - date_depart.year) * 12 + (aujourdhui.month - date_depart.month)
if aujourdhui.day < 2: nb_mois -= 1
investi = 63.85 + (nb_mois * 35)

# --- INTERFACE ---
st.info(f"**MONTANT INVESTI** : {investi:.2f} €")

actuel = st.number_input("**MONTANT ACTUEL (€)**", value=59.57, step=0.01)

if actuel:
    diff = actuel - investi
    perf = (diff / investi) * 100 if investi != 0 else 0
    couleur = "green" if diff >= 0 else "red"
    
    st.markdown(f"""
    <div style="border: 2px solid #1976D2; border-radius: 10px; padding: 20px; text-align: center;">
        <h3 style="color: #1976D2;">PERFORMANCE</h3>
        <h2 style="color: {couleur};">{perf:+.2f} %</h2>
        <h4 style="color: {couleur};">{diff:+.2f} €</h4>
    </div>
    """, unsafe_allow_html=True)