import pandas as pd

# Carrega os dados do arquivo CSV para dentro de um DataFrame
dados = pd.read_csv(r"Exercicio Desafio\Exercicio_16\dados_clientes.csv")

# Calcula a média das idades dos clientes
media_idade = dados["Idade"].mean()

# Calcula a média da renda dos clientes
media_renda = dados["Renda"].mean()

# Encontra a cidade que mais aparece no arquivo
cidade_mais = dados["Cidade"].mode()[0]

# Filtra apenas os clientes com renda acima de 4000
clientes_filt = dados[dados["Renda"] > 4000]

# Exibe a média das idades
print("|Média de idade:", media_idade)

# Exibe a média das rendas
print("|Média de renda:", media_renda)

# Exibe a cidade com maior quantidade de clientes
print("|Cidade com mais clientes:", cidade_mais)

# Titulo da listagem de clientes filtrados
print("\n|Clientes com renda acima de 4000:")

# Exibe os clientes encontrados pelo filtro
print(clientes_filt)