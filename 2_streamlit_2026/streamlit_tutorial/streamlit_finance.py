import pandas as pd
import streamlit as st
import yfinance as yf


st.write(
    """
        # This is my Heading
        
        This is some description of my app
    """
)


import datetime

col1, col2 = st.columns(2)

import datetime

with col1:
    start_date = st.date_input("Please enter Starting Date",
                  datetime.date(2024,1,1))

with col2:
    end_date = st.date_input("Please enter Starting Date",
                  datetime.date(2026,2,1))


import yfinance as yf
ticker_symbol = st.text_input("Enter Stock Symbol",
                              "AAPL",
                              key="placeholder")


ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(start=f"{start_date}",
                                end=f"{end_date}")

st.dataframe(ticker_df)


st.write(
    """
       ## Daily Closing Price Chart
    """
)
st.line_chart(ticker_df.Close)

st.write(
    """
        ## Volume of Shares Traded Each Day
    """
)
st.line_chart(ticker_df.Volume)
