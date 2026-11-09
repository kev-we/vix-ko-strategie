import streamlit as st
import yfinance as yf

st.title("VIX-KO-Strategie")
st.write("Hallo Kevin")

sparrate = st.slider("Monatliche Sparrate (€)", 50, 5000, 200)
st.write("Nach einem Jahr eingezahlt:", sparrate * 12, "€")

zeitraum = st.selectbox("Zeitraum", ["1mo", "6mo", "1y", "5y", "max"], index=2)

@st.cache_data
def lade_kurse(ticker, zeitraum):
    return yf.Ticker(ticker).history(period=zeitraum)

daten = lade_kurse("^GSPC", zeitraum)

# 3. Anzeigen
letzter_kurs = daten["Close"].iloc[-1]
st.metric("S&P 500 – letzter Schlusskurs", f"{letzter_kurs:,.2f}")

st.line_chart(daten["Close"])

st.subheader("Die letzten 5 Tage")
st.dataframe(daten.tail())