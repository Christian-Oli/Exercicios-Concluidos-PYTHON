# Importa a biblioteca responsavel manipula com arquivos CSV
import csv

# Variavel utilizada para armazenar a maior quantidade vendida encontrada
maior_quantidade = 0

# Abre o arquivo CSV em modo de leitura
with open(r"exercicio avançado\Exercicio_15\Magazine.csv", "r", encoding="utf-8") as magazine:

    # Converte o arquivo em um leitor CSV utilizando virgula como separador
    arquivo_csv = csv.reader(magazine, delimiter=",")

    # Pula a primeira linha do arquivo
    next(arquivo_csv)

    # Variavel responsavel por acumular o valor total das vendas
    total_vendas = 0

    # Variavel responsavel por armazenar o produto mais vendido
    produto_popular = ""

    # Laço responsavel por percorrer todas as linhas do arquivo
    for linha in arquivo_csv:

        # Captura o nome do produto
        produto = linha[0]

        # Captura a quantidade vendida
        quantidade = int(linha[1])

        # Captura o preço atual do produto
        preco_atual = float(linha[2])

        # Calcula o valor total vendido daquele produto
        total_vendido = preco_atual * quantidade

        # Exibe as informações do produto e o total arrecadado
        print(f"{produto} vendeu uma quantidade de {quantidade} por R${preco_atual} Reais dando o total de: {total_vendido:.2f}")

        # Soma o valor vendido ao total geral das vendas
        total_vendas += total_vendido

        # Verifica se a quantidade atual é maior que a registrada anteriormente
        if quantidade > maior_quantidade:

            # Atualiza a maior quantidade encontrada
            maior_quantidade = quantidade

            # Guarda o nome do produto mais vendido
            produto_popular = produto

# Exibe qual produto teve a maior quantidade vendida
print(f"O produto {produto_popular} foi vendido em maior quantidade: {maior_quantidade} vendidos")

# Exibe o valor total arrecadado com as vendas
print(f"Total de Vendas: {total_vendas:.2f}")