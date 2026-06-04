
import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV para dentro de um DataFrame
dados = pd.read_csv(r"Exercicio Desafio\Exercicio_16\dados_clientes.csv")

# Conta quantos clientes existem em cada cidade
cidades = dados["Cidade"].value_counts()

# Define o tamanho da janela do gráfico
plt.figure(figsize=(8,5))

# Cria um gráfico de barras utilizando as cidades e suas quantidades
plt.bar(cidades.index, cidades.values)

# Define o titulo do gráfico
plt.title("|Distribuição de Clientes por Cidade|")

# Define o nome do eixo X
plt.xlabel("|Cidade|")

# Define o nome do eixo Y
plt.ylabel("|Quantidade de Clientes|")

# Ajusta automaticamente os elementos do gráfico
plt.tight_layout()

# Exibe o gráfico na tela
plt.show()