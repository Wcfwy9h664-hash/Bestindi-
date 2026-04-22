import streamlit as st
import time
import random

st.set_page_config(page_title="System Terminal - Transaction", layout="centered")

# Style Matrix / Terminal
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
    .terminal-text { line-height: 1.2; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

if 'processed' not in st.session_state:
    st.session_state.processed = False

if not st.session_state.processed:
    st.text("--- INITIALIZING GITHUB DEPLOYMENT ---")
    placeholder = st.empty()
    logs = ""
    
    # Simulation de lignes de code GitHub
    actions = [
        "Fetching origin/master...",
        "Authenticating with Banking Gateway...",
        "Encryption Key: AES-256 Verified.",
        "Connecting to Nasdaq Liquidity Provider...",
        "Bypassing firewall protocols...",
        "Executing: transfer_funds.py --amount 7500 --user 'Tarradas Loic'",
        "Synchronizing blockchain ledger...",
        "Verifying transaction hash: 0x7f88...9a2e",
        "Finalizing smart contract..."
    ]
    
    for action in actions:
        logs += f"> {action}\n"
        placeholder.code(logs)
        time.sleep(random.uniform(0.3, 0.8))
    
    st.session_state.processed = True
    st.rerun()

else:
    # L'affichage final après le faux chargement
    st.balloons()
    st.markdown("""
        <div style="background-color: #1e1e1e; padding: 40px; border-radius: 15px; border: 2px solid #00ff41; text-align: center;">
            <h1 style="color: #00ff41;">✅ TRANSACTION SÉCURISÉE</h1>
            <hr style="border-color: #00ff41;">
            <h2 style="color: white;">DEMANDE DE PAIEMENT ACCEPTÉE</h2>
            <p style="font-size: 30px; color: #00ff41; font-weight: bold;">7 500.00 $</p>
            <p style="color: #aaaaaa; font-size: 18px;">Bénéficiaire :</p>
            <h3 style="color: white;">Monsieur Tarradas Loic</h3>
            <p style="color: #444; font-size: 12px; margin-top: 20px;">Hash: 9e32-88af-7712-bc90-LQ-LOIC</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Réinitialiser le terminal"):
        st.session_state.processed = False
        st.rerun()
