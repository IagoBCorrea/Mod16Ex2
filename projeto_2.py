import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Configurações do tema do Seaborn
sns.set_theme(context='talk', style='ticks')

# Configurações da página no Streamlit
st.set_page_config(
     page_title="Análise Exploratória da Previsão de Renda, por Iago Barbosa Correa",
     page_icon=":bar_chart:",
     layout="wide",
)

# Título principal
st.write('# Análise Exploratória da Previsão de Renda, por Iago Barbosa Correa')

# Carregando o dataset
renda = pd.read_csv('./input/previsao_de_renda.csv')

# Gráficos ao longo do tempo
fig, ax = plt.subplots(8, 1, figsize=(10, 70))

# Histograma para 'posse_de_imovel' e 'renda'
renda[['posse_de_imovel','renda']].plot(kind='hist', ax=ax[0])

# Gráficos de linhas
st.write('## Gráficos ao longo do tempo')
sns.lineplot(x='data_ref', y='renda', hue='posse_de_imovel', data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref', y='renda', hue='posse_de_veiculo', data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref', y='renda', hue='qtd_filhos', data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref', y='renda', hue='tipo_renda', data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=45)

sns.lineplot(x='data_ref', y='renda', hue='tipo_residencia', data=renda, ax=ax[7])
ax[7].tick_params(axis='x', rotation=45)

# Remove bordas extras dos gráficos
sns.despine()

# Exibe o gráfico de linhas no Streamlit
st.pyplot(plt)

# Gráficos bivariados (renda por categoria)
st.write('## Gráficos Bivariados')
fig, ax = plt.subplots(7, 1, figsize=(10, 50))

sns.barplot(x='posse_de_imovel', y='renda', data=renda, ax=ax[0])
sns.barplot(x='posse_de_veiculo', y='renda', data=renda, ax=ax[1])
sns.barplot(x='qtd_filhos', y='renda', data=renda, ax=ax[2])
sns.barplot(x='tipo_renda', y='renda', data=renda, ax=ax[3])
sns.barplot(x='educacao', y='renda', data=renda, ax=ax[4])
sns.barplot(x='estado_civil', y='renda', data=renda, ax=ax[5])
sns.barplot(x='tipo_residencia', y='renda', data=renda, ax=ax[6])

# Remove bordas extras dos gráficos
sns.despine()

# Exibe os gráficos bivariados no Streamlit
st.pyplot(plt)
