import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Dashboard de Churn",
    layout="wide"
)

df = pd.read_csv("data/merchant_churn.csv")

st.title("Dashboard de Churn de Comerciantes")

st.subheader("Distribuição dos comerciantes por setor")

fig_setor_1, ax = plt.subplots()

sns.countplot(data=df, y='industry', ax=ax)

fig_setor_2, ax = plt.subplots()
contagem_setor = df['industry'].value_counts()
ax.bar(contagem_setor.index, contagem_setor.values) #OBS: melhor colocar na horizontal
ax.set_title("Distribuição por Setor")
ax.set_xlabel("Setor")
ax.set_ylabel("Quantidade")


col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig_setor_1)
with col2:
    st.pyplot(fig_setor_2)

