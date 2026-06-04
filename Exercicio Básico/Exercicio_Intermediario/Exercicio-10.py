# Variavel responsavel pela escolha do menu principal
escolha = 0

# Variavel utilizada para armazenar a temperatura digitada
valor = 0

# Linha divisoria para melhorar a visualização da aplicação
__divider = print("-" * 50)

# Variavel responsavel pelos calculos intermediarios
resultado_temp = 0

# Variavel responsavel por armazenar o resultado final
resultado_total = 0

# Variavel utilizada para limpar os valores utilizados anteriormente
limpeza = valor = resultado_temp = resultado_total = 0

# Função para converter Celcius em Fahrenheit
def fahrenheit():

    # Exibe a linha divisoria
    print("-" * 50)

    # Recebe a temperatura digitada pelo usuario
    valor = float(input("Digite aqui a temperatura desejada:"))

    # Realiza a primeira parte do calculo
    resultado_temp = valor * 1.8

    # Soma 32 para obter Fahrenheit
    resultado_total = resultado_temp + 32

    # Exibe a linha divisoria
    print("-" * 50)

    # Mostra o resultado da conversão
    print(f"Sua temperatura em fahrenheit é: {resultado_total:.1f}F")

    # Exibe a linha divisoria
    print("-" * 50)

    # Limpa os valores utilizados
    limpeza

# Função para converter Fahrenheit em Celcius
def celcius():

    # Exibe a linha divisoria
    print("-" * 50)

    # Recebe a temperatura digitada pelo usuario
    valor = float(input("Digite aqui a temperatura desejada:"))

    # Realiza a primeira parte do calculo
    resultado_temp = valor - 32

    # Divide por 1.8 para obter Celcius
    resultado_total = resultado_temp / 1.8

    # Exibe a linha divisoria
    print("-" * 50)

    # Mostra o resultado da conversão
    print(f"Sua temperatura em celcius é: {resultado_total:.1f}°")

    # Exibe a linha divisoria
    print("-" * 50)

    # Limpa os valores utilizados
    limpeza

# Laço principal da aplicação
while True:

    # Exibe a linha divisoria
    __divider

    # Titulo da aplicação
    print("Termormeter: Conversor de Temperatura")

    # Exibe as opções disponiveis
    print("(1)- Fahrenheit\n(2)- Celcius\n(3)- Sair \n ")

    # Recebe a escolha do usuario
    escolha = int(input("Digite aqui sua opção:"))

    # Exibe a linha divisoria
    __divider

    # Verifica qual opção foi escolhida
    if escolha == 1:

        # Chama a função de conversão para Fahrenheit
        fahrenheit()

    else:

        if escolha == 2:

            # Chama a função de conversão para Celcius
            celcius()

        else:

            if escolha == 3:

                # Encerra a aplicação
                break

            else:

                # Alerta caso a opção seja invalida
                print("Escolha invalida! Tente novamente...")