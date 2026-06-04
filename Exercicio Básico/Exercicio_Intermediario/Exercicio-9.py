# Variavel que irá receber o numero digitado pelo usuario
numero_u = 0

# Variavel auxiliar para realizar os calculos do fatorial
numero_t = 0

# Variavel responsavel por armazenar o resultado final
resultado = 0

# Limite utilizado para controlar o laço
limite = 3

# Input que recebe o numero para calcular o fatorial
numero_u = int(input("Digite aqui seu número fatorial:"))

# Copia o valor digitado para a variavel auxiliar
numero_t = numero_u

# Exibe o numero digitado pelo usuario
print(numero_t)

# Laço responsavel por realizar as multiplicações do fatorial
while numero_t >= limite:

    # Verifica se é a primeira passagem pelo laço
    if numero_t == numero_u:

        # Diminui 1 do numero atual
        numero_t -= 1

        # Realiza a primeira multiplicação
        resultado = numero_u * numero_t

        # Exibe o resultado parcial
        print(resultado)

    else:

        # Diminui 1 do numero atual
        numero_t -= 1

        # Continua as multiplicações do fatorial
        resultado = resultado * numero_t

        # Exibe o resultado parcial
        print(resultado)