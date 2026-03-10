import streamlit as st

st.title("⚽ Trading Over/Under")

st.header("Dati partita")

squadra1 = st.text_input("Squadra casa")
squadra2 = st.text_input("Squadra ospite")

quota_over25 = st.number_input("Quota Over 2.5", step=0.01)

minuto = st.number_input("Minuto partita", step=1)

gol_casa = st.number_input("Gol casa", step=1)
gol_trasferta = st.number_input("Gol trasferta", step=1)

gol_tot = gol_casa + gol_trasferta

st.write("Gol totali:", gol_tot)

quota_under25 = st.number_input("Quota Under 2.5", step=0.01)

if st.button("Calcola strategia"):

    if minuto < 30 and quota_over25 >= 1.80:
        st.write("Entrata possibile su Over 2.5")

    elif minuto >= 30 and gol_tot == 0 and quota_over25 >= 2.00:
        st.write("Entrata ritardata Over 2.5")

    elif gol_tot == 1:
        st.write("Possibile copertura Over 1.5")

    else:
        st.write("Partita da evitare")
