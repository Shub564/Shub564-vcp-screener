import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 VCP Stock Screener")

st.write("Yeh ek basic demo hai jo stock ka price data dikhata hai.")

ticker = st.text_input("Enter Stock Symbol (e.g., TCS.NS)", "TCS.NS")

if ticker:
    data = yf.download(ticker, period="6mo", interval="1d")
    st.line_chart(data['Close'])
