import streamlit as st

st.title("⚽ Over Trading Assistant PRO")

st.header("Dati partita")

squadra1 = st.text_input("Squadra casa")
squadra2 = st.text_input("Squadra ospite")

quota_over25 = st.number_input("Quota Over 2.5", step=0.01)
stake = st.number_input("Stake Over", step=1)

st.header("Dati Live")

minuto = st.number_input("Minuto partita", step=1)

gol_casa = st.number_input("Gol casa", step=1)
gol_trasferta = st.number_input("Gol ospite", step=1)

gol_tot = gol_casa + gol_trasferta

st.write("Gol totali:", gol_tot)

tiri = st.number_input("Tiri totali", step=1)
tiri_porta = st.number_input("Tiri in porta", step=1)
attacchi = st.number_input("Attacchi pericolosi", step=1)
xg = st.number_input("Expected goals (xG)", step=0.1)

quota_under25 = st.number_input("Quota Under 2.5", step=0.01)
quota_under15 = st.number_input("Quota Under 1.5", step=0.01)
quota_under05 = st.number_input("Quota Under 0.5", step=0.01)

if st.button("Analizza partita"):

    punteggio = 0

    if tiri >= 8:
        punteggio += 2

    if tiri_porta >= 3:
        punteggio += 2

    if attacchi >= 20:
        punteggio += 2

    if xg >= 1:
        punteggio += 3

    if minuto >= 35 and minuto <= 65 and gol_tot == 0:
        punteggio += 3

    st.subheader("Punteggio partita")
    st.write(punteggio)

    if punteggio >= 8:
        st.success("🔥 PARTITA OTTIMA PER OVER")

    elif punteggio >= 5:
        st.warning("⚠️ PARTITA INTERESSANTE")

    else:
        st.error("❌ PARTITA DA EVITARE")

    if punteggio >= 8 and gol_tot == 0 and minuto >= 35:
        st.write("Strategia: entrare su Over 2.5")

    if gol_tot == 1:
        st.write("Strategia: possibile copertura Over 1.5")

    if gol_tot == 0 and minuto >= 60:
        st.write("Strategia: valutare copertura")

    st.subheader("Calcolo coperture")

    if quota_under25 > 1:
        stake25 = round(stake / (quota_under25 - 1), 2)
        st.write("Copertura Under 2.5:", stake25, "€")

    if quota_under15 > 1:
        stake15 = round(stake / (quota_under15 - 1), 2)
        st.write("Copertura Under 1.5:", stake15, "€")

    if quota_under05 > 1:
        stake05 = round(stake / (quota_under05 - 1), 2)
        st.write("Copertura Under 0.5:", stake05, "€")
    
