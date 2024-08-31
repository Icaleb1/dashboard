import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ativar o layout amplo no início
st.set_page_config(layout="wide")

# Estilo CSS customizado para remover margens (opcional)
st.markdown("""
    <style>
        .css-18e3th9 { padding: 0px 0px; }
        .css-1d391kg { padding: 0px; }
        .css-1dbjc4n { padding: 0px 0px; }
    </style>
    """, unsafe_allow_html=True)

# Dados de horas trabalhadas (exemplo)
data = {
    'Funcionário': ['Funcionário 1', 'Funcionário 2', 'Funcionário 3'],
    'Horas Antes': [40, 35, 40],  # Horas por semana
    'Horas Depois': [10, 8, 10],  # Horas por semana após automação
}

df = pd.DataFrame(data)

# Cálculos de redução
df['Horas Economizadas'] = df['Horas Antes'] - df['Horas Depois']
df['Redução (%)'] = (df['Horas Economizadas'] / df['Horas Antes']) * 100

# Título do Dashboard
st.title('Redução de Trabalho com Automação de WhatsApp')

# Criação das colunas com nova proporção
col1, col2 = st.columns([1, 2])  # Aumentar o tamanho da tabela

# Gráfico de barras na primeira coluna (menor)
st.subheader('Comparação de Horas Trabalhadas por Funcionário')
fig, ax = plt.subplots(figsize=(12, 6))  # Ajustar o tamanho do gráfico
bar_width = 0.35
index = df.index

ax.bar(index, df['Horas Antes'], bar_width, label='Antes da Automação', color='skyblue')
ax.bar(index + bar_width, df['Horas Depois'], bar_width, label='Depois da Automação', color='lightgreen')

ax.set_xlabel('Funcionários')
ax.set_ylabel('Horas por Semana')
ax.set_title('Horas Trabalhadas Antes e Depois da Automação')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(df['Funcionário'])
ax.legend()

st.pyplot(fig)

# Tabela na segunda coluna (maior)

st.subheader('Detalhamento por Funcionário')
st.table(df[['Funcionário', 'Horas Antes', 'Horas Depois', 'Horas Economizadas', 'Redução (%)']])

# Métricas de resumo abaixo
st.subheader('Resumo da Redução de Trabalho')
total_horas_antes = df['Horas Antes'].sum()
total_horas_depois = df['Horas Depois'].sum()
total_horas_economizadas = df['Horas Economizadas'].sum()
percentual_reducao = (total_horas_economizadas / total_horas_antes) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Horas Antes", f"{total_horas_antes}h")
col2.metric("Total Horas Depois", f"{total_horas_depois}h")
col3.metric("Horas Economizadas", f"{total_horas_economizadas}h")
col4.metric("Redução Total", f"{percentual_reducao:.2f}%")
