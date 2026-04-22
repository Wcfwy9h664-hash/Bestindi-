import streamlit as st
import time

# Configuration de la page
st.set_page_config(page_title="Confirmation de Paiement", page_icon="✅")

# Style CSS pour faire "Pro"
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stAlert {
        border-radius: 15px;
    }
    .success-text {
        color: #09ab3b;
        font-weight: bold;
        font-size: 24px;
        text-align: center;
    }
    .payment-card {
        background-color: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Simulation d'un chargement pour le réalisme
with st.spinner('Vérification de la transaction...'):
    time.sleep(1.5)

# Conteneur central
st.markdown('<div class="payment-card">', unsafe_allow_html=True)

st.success("### ✅ Paiement Accepté")

st.markdown("---")

# Détails du paiement
st.write("#### Détails du transfert")
col1, col2 = st.columns(2)

with col1:
    st.write("**Bénéficiaire :**")
    st.write("**Montant :**")
    st.write("**Statut :**")
    st.write("**Référence :**")

with col2:
    st.write("Monsieur **Tarradas Loic**")
    st.write("7 500.00 $")
    st.write("✨ Confirmé")
    st.write("TRX-992847561-NAS")

st.markdown("---")

st.info("Le montant de **7 500 $** a été crédité sur votre compte avec succès.")

if st.button("Télécharger le reçu PDF"):
    st.balloons()
    st.write("Génération du reçu en cours...")

st.markdown('</div>', unsafe_allow_html=True)

# Petit message de pied de page
st.caption("Transaction sécurisée par le protocole SSL 256-bit")
