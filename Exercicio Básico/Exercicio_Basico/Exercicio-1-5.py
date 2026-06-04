# Inicio pra estabelecer o usuario do aplicativo, não havia necessidade mas quis adicionar.
print("Antes de começar, primeiro precisamos saber o seu nome.")
usuario = input("Digite seu nome aqui:\n")

# variavel para não poluir o codigo.
espaço_tela = print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")

# Pequeno Texto de Saudação.
print("================================================")
print("Olá usuário,", usuario,"seja bem vindo(a) ao aplicativo Calc-Master")
print("================================================")
# Função para opção Calculo simples
def calc_simples():
    espaço_tela
    # Titulo do Menu
    print("================================================")
    print("=============Calculadora Simples===============")
    print("================================================")
    # Duas variaveis para captura valores inteiros. 
    numero_o = int(input(f"{usuario} Digite o primeiro numero:"))
    numero_t = int(input(f"{usuario} Digite o segundo numero:"))
    print("================================================")
    # Coloca o resultado dos calculos entre numero_o e numero_t dentro de variaveis.
    soma = numero_o + numero_t
    subtracao = numero_o - numero_t
    multiplicao = numero_o * numero_t
    divisao = numero_o / numero_t

    espaço_tela
    # Titulo do resultado
    print("================================================")
    print("Seu numeros são (", numero_o, numero_t,") e aqui estão os resultados", usuario)
    print("Subtração dos numeros:", subtracao)
    print("Soma do numeros", soma)
    print("Multiplicação dos numeros:", multiplicao)
    print(f"Divisão dos numeros são:{divisao:.2f}")
    print("================================================")

def impar_par():
    espaço_tela
    # Titulo do Menu    
    print("================================================")
    print("========Indentificador de par ou impar==========")
    print("================================================")
    # Input responsavel por pegar um numero inteiro dado pelo usuario
    numero_p = int(input(f"{usuario} digite aqui o numero:"))

    # Um if para dividir o numero_p por 2, se ele for dividido por 2 e resta 0 será "printado" par.
    if numero_p % 2 == 0:
        print("================================================")
        print(f"{usuario} o número", numero_p," é um Par.")
        print("================================================")
    # Porém, caso ele não resta 0 irá printar impar. 
    else:
        print("================================================")
        print(f"{usuario} o número", numero_p," é um Impar.")
        print("================================================")

def tabuadas():
    # Resgatará um numero inteiro do usuario.
    numero_ta = int(input("{usuario} digite aqui o numero:"))

    # Variaveis usadas para percorrer a lista
    i = 0
    y = 0
    w = 0
    z = 0
    # Variavel responsavel pelo controle de resultados
    resultado = 0
    # Variavel responsavel pela limpeza da variavel resultado para a proxima tabuada
    limpeza = resultado = 0
    limpeza_c = i = y = w = z = 0

    print("================================================")
    print("==============Tabuada de Soma===================")
    print("================================================")
    # Um while capaz de pecorrer até 10
    while i <= 10:
        # Calculo feito na "casa" atual
        resultado = i + numero_ta
        # Ele irá printa toda vez que o calculo for feito
        print("==============", i, "+", numero_ta, "=", resultado, "=====================")
        # Contabilizador da "casa"
        i += 1
        

    limpeza
    limpeza_c

    print("================================================")
    print("==============Tabuada de Subtração==============")
    print("================================================")
     # Um while capaz de pecorrer até 10
    while y <= 10:
        # Calculo feito na "casa" atual
        resultado = numero_ta - y
        # Estava tendo dificuldade e usei essa transformador de numero negativo para positivo
        positivo = abs(resultado)
        # Ele irá printa toda vez que o calculo for feito
        print("==============", y, "-", numero_ta, "=", positivo, "=====================")
        # Contabilizador da "casa"
        y += 1        

    limpeza
    limpeza_c

    print("================================================")
    print("==============Tabuada de Multiplicação==========")
    print("================================================")
    # Um while capaz de pecorrer até 10
    while w <= 10:
        # Calculo feito na "casa" atual
        resultado = w * numero_ta
        # Ele irá printa toda vez que o calculo for feito
        print("==============", w, "x", numero_ta, "=", resultado, "=====================")
        # Contabilizador da "casa"
        w += 1

    limpeza
    limpeza_c

    print("================================================")
    print("==============Tabuada de divisão================")
    print("================================================")
    # Um while capaz de pecorrer até 10
    while z <= 10:
        # Calculo feito na "casa" atual
        resultado = z * numero_ta
        # Ele irá printa toda vez que o calculo for feito
        print("==============", resultado, "/", numero_ta, "=", z, "=====================")
        # Contabilizador da "casa"
        z += 1
    
    limpeza
    limpeza_c

    

def media():
    # Inputs necessarios para capturar a nota do usuario
    numero_m1 = float(input(f"{usuario} digite seu nota aqui:"))
    numero_m2 = float(input(f"{usuario} digite seu nota aqui:"))
    numero_m3 = float(input(f"{usuario} digite seu nota aqui:"))
    # Somar as notas entre elas e dividir por 3
    resultado = (numero_m1 + numero_m2 + numero_m3) / 3
    # If necessario para delimitar que o aluno foi ou não aprovado.
    if resultado >= 6:
        # Caso o resultaado for maior ou igual a 6 está aprovado.
        print(f"Aluno foi aprovado! Seu resultado foi:{resultado:.2f}" )
    else:
        # Caso for menor, será reprovado.
        print(f"O aluno foi reprovado! Seu resultado foi:{resultado:.2f}")

while True:
    # Titulo do Menu  
    print("================================================")
    print("========Menu da Aplicação de Cálculos:==========")
    print("================================================")
    # Print responsavel por mostrar as opções
    print("1- Calculadora Simples \n 2- Impar ou par \n 3- Tabuada \n 4- Media de Notas")
    # Input responsavel pelo controle de escolha. 
    escolha = int(input(f"{usuario} digite aqui a opção desejada:\n"))
    # Um if que vai se descontruindo até levar usuario a interface desejada
    if escolha == 1:
        calc_simples()
    else: 
        if escolha == 2:
            impar_par()
        else: 
            if escolha == 3:
                tabuadas()
            else:
                if escolha == 4:
                    media()
                else:
                    print("Opção invalida")
                    continue