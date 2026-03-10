import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Over Trading",layout="centered")

st.title("⚽ SMART OVER TRADING ELITE")

st.header("Dati partita")

home = st.text_input("Squadra casa")
away = st.text_input("Squadra ospite")

quota_over = st.number_input("Quota Over 2.5",step=0.01)
stake = st.number_input("Stake Over (€)",step=1)

st.header("Dati LIVE")

minute = st.number_input("Minuto",step=1)

goal_home = st.number_input("Gol casa",step=1)
goal_away = st.number_input("Gol ospite",step=1)

goals = goal_home + goal_away

shots = st.number_input("Tiri totali",step=1)
shots_on = st.number_input("Tiri in porta",step=1)
danger = st.number_input("Attacchi pericolosi",step=1)
possession = st.number_input("Possesso offensivo (%)",step=1)

xg = st.number_input("Expected Goals (xG)",step=0.1)

quota_u25 = st.number_input("Quota Under 2.5",step=0.01)
quota_u15 = st.number_input("Quota Under 1.5",step=0.01)
quota_u05 = st.number_input("Quota Under 0.5",step=0.01)

if st.button("Analizza partita"):

    # INDICE PRESSIONE
    pressure = (shots_on*4)+(shots*1)+(danger*0.6)+(xg*12)

    # RITMO PARTITA
    tempo = pressure / max(minute,1)

    # INDICE GOAL EXPECTATION
    goal_index = (shots_on*2)+(xg*10)+(danger*0.3)

    score = 0

    if tempo > 1.7:
        score += 4

    if shots_on >= 4:
        score += 3

    if danger >= 30:
        score += 2

    if xg >= 1.3:
        score += 3

    if minute >= 35 and minute <= 70 and goals == 0:
        score += 3

    st.subheader("Indice pressione")
    st.write(round(pressure,2))

    st.subheader("Ritmo partita")
    st.write(round(tempo,2))

    st.subheader("Indice gol atteso")
    st.write(round(goal_index,2))

    st.subheader("Score partita")
    st.write(score)

    # SEMAFORO

    if score >= 11:
        st.success("🟢 MATCH PERFETTO PER OVER")

    elif score >= 7:
        st.warning("🟡 MATCH INTERESSANTE")

    else:
        st.error("🔴 MATCH DA EVITARE")

    # STRATEGIA

    st.subheader("Strategia")

    if score >= 10 and goals == 0 and minute >= 35:
        st.write("🔥 ENTRARE OVER 2.5")

    elif goals == 1 and minute <= 60:
        st.write("⚡ TENERE POSIZIONE")

    elif goals == 1 and minute > 60:
        st.write("⚠️ COPERTURA OVER 1.5")

    elif goals == 0 and minute >= 65:
        st.write("⚠️ VALUTARE HEDGE")

    else:
        st.write("Attendere sviluppo partita")

    # PROBABILITA GOL

    probability = min(95,int(goal_index*3))

    st.subheader("Probabilità gol stimata")

    st.progress(probability/100)

    st.write(str(probability)+" %")

    # COPERTURE

    st.subheader("Calcolo coperture")

    if quota_u25 > 1:
        hedge25 = round(stake/(quota_u25-1),2)
        st.write("Copertura Under 2.5:",hedge25,"€")

    if quota_u15 > 1:
        hedge15 = round(stake/(quota_u15-1),2)
        st.write("Copertura Under 1.5:",hedge15,"€")

    if quota_u05 > 1:
        hedge05 = round(stake/(quota_u05-1),2)
        st.write("Copertura Under 0.5:",hedge05,"€")

    # GRAFICO PRESSIONE

    st.subheader("Grafico pressione")

    data = {
        "Tipo":["Tiri","Tiri Porta","Attacchi","xG"],
        "Valore":[shots,shots_on,danger,xg]
    }

    df = pd.DataFrame(data)

    st.bar_chart(df.set_index("Tipo"))
