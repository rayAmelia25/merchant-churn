import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard de Churn",
    layout="wide"
)

df = pd.read_csv("data/merchant_churn.csv")

st.title("Dashboard de Churn de Comerciantes")

st.subheader("Análise Exploratória")

#st.dataframe(df)

#Tempo de ralacionamento em meses
fig_tempo_relacionamento, ax = plt.subplots()
cont = df['tenure_months'].value_counts()
ax.bar(cont.index, cont.values)
ax.set_title("Distribuição do Tempo do Relacionamento")
ax.set_xlabel("Duração (Meses)")
ax.set_ylabel("Quantidade de Comerciantes")

fig_teste, ax = plt.subplots()
ax = df['tenure_months'].hist(edgecolor='black')
plt.grid(False)
plt.xticks(range(0, 66, 6))
#plt.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_title("Distribuição do Tempo de Relacionamento")
ax.set_xlabel("Duração (Meses)")
ax.set_ylabel("Quantidade de Comerciantes")

fig_receita_mensal, ax = plt.subplots()
ax = df['monthly_revenue'].hist(edgecolor='black')
plt.grid(False)
ax.set_title("Distribuição da Receita Mensal")
#ax.set_xlabel("Receita") 
#ax.set_ylabel("Comerciantes")


# PRIMEIRA linha de graficos
col1, col2, col3 = st.columns(3)
with col1:
    st.pyplot(fig_tempo_relacionamento) #tenho que decidir qual o melhor para usar do tempo de relacionamento (testei dois graficos nessa coluna)
with col2:
    st.pyplot(fig_teste) #o relacionamento teste
with col3:
    st.pyplot(fig_receita_mensal)

fig_volume_transacao, ax = plt.subplots()
ax = df['avg_monthly_txn'].hist(edgecolor='black') # quanto maior a empresa maior o volume de transações
plt.grid(False)
ax.set_title("Volume de Transações")
#ax.set_xlabel("") 
#ax.set_ylabel("")

fig_ticket_medio, ax = plt.subplots()
ax = df['avg_ticket_size'].hist(edgecolor='black') # quanto maior a empresa maior o volume de transações
plt.grid(False)
ax.set_title("Ticket Médio")
#ax.set_xlabel("") 
#ax.set_ylabel("")

fig_satisfacao, ax = plt.subplots()
ax = df['satisfaction_score'].hist(edgecolor='black') # quanto maior a empresa maior o volume de transações
plt.grid(False)
ax.set_title("Satisfação")
#ax.set_xlabel("") 
#ax.set_ylabel("")

# SEGUNDA linha de graficos
col1, col2, col3 = st.columns(3)
with col1:
    st.pyplot(fig_volume_transacao)
with col2:
    st.pyplot(fig_ticket_medio)
with col3:
    st.pyplot(fig_satisfacao)

fig_chamado, ax = plt.subplots()
ax = df['support_tickets_90d'].hist(edgecolor='black') # quanto maior a empresa maior o volume de transações
plt.grid(False)
ax.set_title("Chamados")
#ax.set_xlabel("") 
#ax.set_ylabel("")

fig_pag_falhado, ax = plt.subplots()
ax = df['failed_payments_90d'].hist(edgecolor='black') # quanto maior a empresa maior o volume de transações
plt.grid(False)
ax.set_title("Ticket Médio")
#ax.set_xlabel("") 
#ax.set_ylabel("")

fig_tempo_solu, ax = plt.subplots()
ax = df['avg_resolution_hours'].hist(edgecolor='black') # quanto maior a empresa maior o volume de transações
plt.grid(False)
ax.set_title("Satisfação")
#ax.set_xlabel("") 
#ax.set_ylabel("")

# TERCEIRA linha de graficos
col1, col2, col3 = st.columns(3)
with col1:
    st.pyplot(fig_chamado)
with col2:
    st.pyplot(fig_pag_falhado)
with col3:
    st.pyplot(fig_tempo_solu)