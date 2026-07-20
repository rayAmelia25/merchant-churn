import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

st.set_page_config(
    page_title="Dashboard de Churn",
    layout="wide"
)

df = pd.read_csv("data/merchant_churn.csv")

st.title("Dashboard de Churn de Comerciantes")

st.subheader("Visão Geral dos Comerciantes")

fig_setor_1, ax = plt.subplots()

contagem_setor = df['industry'].value_counts() #
ax.barh(contagem_setor.index, contagem_setor.values) #Grafico de barras horizontal: 
ax.yaxis.set_inverted(True) # inverte a ordem
ax.set_title("Distribuição por Setor")
ax.set_xlabel("Quantidade")
ax.set_ylabel("Setor")

fig_setor_2, ax = plt.subplots()
contagem_tamanho = df['tier'].value_counts()
ax.bar(contagem_tamanho.index, contagem_tamanho.values) #CORRIGIR: o tamanho entre os dois graficos não ficou proporcional
ax.set_title("Distribuição por Tamanho")
ax.set_xlabel("Tamanho da Empresa")
ax.set_ylabel("Quantidade")


col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig_setor_1)
with col2:
    st.pyplot(fig_setor_2)

#Distribuição por região (region).
fig, ax = plt.subplots()
contagem_regiao = df['region'].value_counts()
ax.bar(contagem_regiao.index, contagem_regiao.values)
ax.set_title("Distribuição por Região")
#ax.set_xlabel("Regiões")
ax.set_ylabel("Quantidade")

#Distribuição por região (region).
fig_plano, ax = plt.subplots()
contagem_plano = df['plan'].value_counts()
ax.bar(contagem_plano.index, contagem_plano.values)
ax.set_title("Distribuição por Planos")
#ax.set_xlabel("Tipo de Plano")
ax.set_ylabel("Quantidade")

col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig)
with col2:
    st.pyplot(fig_plano)
