import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Dashboard de Churn",
    layout="wide"
)

df = pd.read_csv("data/merchant_churn.csv")

st.title("Dashboard de Churn de Comerciantes")

st.subheader("Visão Geral dos Comerciantes")