numero_u = 0
numero_t = 0
resultado = 0
limite = 3

numero_u = int(input("Digite aqui seu número fatorial:"))
numero_t = numero_u
print(numero_t)

while numero_t >= limite:
    if numero_t == numero_u:
        numero_t -= 1
        resultado = numero_u * numero_t
        print(resultado)
    else:
        numero_t -= 1
        resultado = resultado * numero_t
        print(resultado)
    
    


