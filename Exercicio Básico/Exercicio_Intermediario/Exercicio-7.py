# Variavel que recebe a palavra digitada pelo usuario
palavra = str(input("Digite aqui sua palavra:"))

# Variavel contendo todas as vogais maiusculas e minusculas
vogais = "aeiouAEIOU"

# Variavel responsavel por contar a quantidade de vogais
contador = 0

# Laço que percorre cada letra da palavra
for letras in palavra:
    
    # Verifica se a letra atual é uma vogal
    if letras in vogais:
        
        # Caso seja vogal, adiciona 1 ao contador
        contador += 1

# Exibe a quantidade total de vogais encontradas
print(contador)