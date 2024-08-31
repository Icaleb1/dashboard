import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dados de exemplo
data = {
    'Funcionário-ID': [1, 2, 3, 1, 2],
    'horasTrabalhoExcel': [1, 2, 3, 1, 1],
    'Dia': [1, 2, 3, 4, 5],
    'TipoCliente': ['Inadimplentes', 'Oportunidade', 'Ausente', '', ''],
    'TotalClientes': [50, 30, 10, None, None],
    'TempoDeEnvio': [None, None, None, None, None]
}

df = pd.DataFrame(data)

# Preencher valores ausentes com 0 para simplificação
df['TotalClientes'].fillna(0, inplace=True)

# Calcular o tempo total gasto
tempo_total = df.groupby('TipoCliente')['TotalClientes'].sum()

# Tempo total gasto por dia
tempo_por_dia = df.groupby('Dia')['horasTrabalhoExcel'].sum()

# Tempo total gasto por funcionário
tempo_por_funcionario = df.groupby('Funcionário-ID')['horasTrabalhoExcel'].sum()

# Streamlit app
st.title('Dashboard de Tempo de Envio de Mensagens')

st.header('Tempo Gasto por Tipo de Cliente')
st.bar_chart(tempo_total)

st.header('Tempo Gasto por Dia Útil')
st.line_chart(tempo_por_dia)

st.header('Tempo Gasto por Funcionário')
st.bar_chart(tempo_por_funcionario)

# Gráficos adicionais
st.write('Gráficos adicionais e insights podem ser adicionados aqui.')

