palavra = str(input("Digite aqui sua palavra:"))
vogais = "aeiouAEIOU"
contador = 0


for letras in palavra:
    if letras in vogais:
        contador +=1
print(contador)

