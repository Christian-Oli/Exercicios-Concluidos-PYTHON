escolha = 0
valor = 0
__divider = print("-" * 50)
resultado_temp = 0
resultado_total = 0
limpeza = valor = resultado_temp = resultado_total = 0

def fahrenheit():
    print("-" * 50)
    valor = float(input("Digite aqui a temperatura desejada:"))
    resultado_temp = valor * 1.8
    resultado_total = resultado_temp + 32
    print("-" * 50)
    print(f"Sua temperatura em fahrenheit é: {resultado_total:.1f}F")
    print("-" * 50)
    limpeza

def celcius():
    print("-" * 50)
    valor = float(input("Digite aqui a temperatura desejada:"))
    resultado_temp = valor - 32
    resultado_total = resultado_temp / 1.8
    print("-" * 50)
    print(f"Sua temperatura em celcius é: {resultado_total:.1f}°")
    print("-" * 50)
    limpeza

while True:
    __divider
    print("Termormeter: Conversor de Temperatura")
    print("(1)- Fahrenheit\n(2)- Celcius\n(3)- Sair \n ")
    escolha = int(input("Digite aqui sua opção:"))
    __divider
    if escolha == 1:
        fahrenheit()
    else:
        if escolha == 2:
            celcius()
        else:
            if escolha == 3:
                break
            else:
                print("Escolha invalida! Tente novamente...")
