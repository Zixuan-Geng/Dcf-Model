import streamlit as st
from dcf import run_dcf
from data import get_financials, get_shares_outstanding

st.title("DCF Valuation Model")

ticker = st.text_input("Enter Stock Ticker", value="AAPL")
fcf_growth = st.slider("FCF Growth Rate", 0.01, 0.30, 0.10)
terminal_growth = st.slider("Terminal Growth Rate", 0.01, 0.05, 0.025)
wacc = st.slider("WACC", 0.05, 0.20, 0.09)

if st.button("Run Valuation"):
    base_fcf = get_financials(ticker)
    shares = get_shares_outstanding(ticker)
    result = run_dcf(base_fcf, fcf_growth, terminal_growth, wacc, shares)
    st.metric("Price Per Share", f"${result['Price Per Share']}")
    st.metric("Enterprise Value", f"${result['Enterprise Value']:,.0f}")
    st.metric("Terminal Value", f"${result['Terminal Value']:,.0f}")
    st.write("Projected FCFs:", result["Projected FCFs"])
