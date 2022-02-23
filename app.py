import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import time

st.title("GROUP 3 FINAL PROJECT")
st.markdown("Streamlit graphs")

add_selectbox = st.sidebar.selectbox("How would you like to be contacted?",
                                     ("Email", "Home phone", "Mobile phone"))
st.sidebar.button("hello")

#climate
st.write("climate Data")
df = pd.read_csv("D:\group3\group3\climate.csv")

df = df.rename(columns={'year': 'index'}).set_index('index')

st.write(df)
chart_data = pd.DataFrame(df, columns=["annual_rainfall"])

st.bar_chart(chart_data)
# st.bar_chart(df)

# #food_produced_percapita
st.write("food_produced_percapita Data")
df1 = pd.read_csv("food.csv")
df1 = df1.rename(columns={'year': 'index'}).set_index('index')
st.write(df1.head())
st.bar_chart(df1)

#CPI
st.write("CPI DATA")
df2 = pd.read_csv("D:\group3\group3\cpi.csv")
df2 = df2.rename(columns={'year': 'index'}).set_index('index')
st.write(df2.head())
st.bar_chart(df2)

# #Commodity Prices since 2004
st.write("Commodity Prices since 2004")
df3 = pd.read_csv("D:\group3\group3\commodity_prices.csv")

st.write(df3.head())

#Project Analysis
st.write("Project Analysis Data")
df_maize = pd.read_csv("maize_data.csv")

df_maize = df_maize.rename(columns={'year': 'index'}).set_index('index')
chart_data = pd.DataFrame(df_maize, columns=["price of maize"])
st.write(df_maize.head())
st.bar_chart(chart_data)
st.line_chart(df_maize)