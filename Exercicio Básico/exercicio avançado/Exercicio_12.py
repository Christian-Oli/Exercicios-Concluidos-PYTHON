
import string
import random

# Variavel responsavel por armazenar o limite da senha
limite = 0

# Variavel contendo numeros, letras e caracteres especiais
alimentador = string.digits + string.ascii_letters + string.punctuation

# Lista responsavel por armazenar os caracteres da senha
senha = []

# Titulo da aplicação
print("Gerador de Senha\n")

# Input que recebe a quantidade de caracteres desejada
limite = int(input("digite aqui o Limite de Caracteres:\n"))

# Laço responsavel por gerar a quantidade de caracteres escolhida
for i in range(limite):

    # Escolhe um caractere aleatorio do alimentador
    letra = random.choice(alimentador)

    # Adiciona o caractere escolhido na lista da senha
    senha.append(letra)

# Converte a lista em uma unica string
senha = ''.join(senha)

# Exibe uma mensagem informando o resultado
print("Sua senha gerada corresponde:")

# Exibe a senha gerada
print(senha)