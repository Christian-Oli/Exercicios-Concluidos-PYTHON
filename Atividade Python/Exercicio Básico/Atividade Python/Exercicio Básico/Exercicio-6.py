lista = []
historico = []

def adicionar():
    opcao = 0
    while opcao == 0:
        item = input("Digite aqui o item que deseja em sua lista de desejos:\n")
        opcao = int(input("Tem certeza em adicionar esse item? (1-Sim) (2-Não)"))
        if opcao == 1:
            print(f"Você adicionou o item: {item}!")
            lista.append(item)
            historico.append(item)
        else:
            print(f"Você não adicionou: {item}")
            item = ""
            opcao = 0
            continue

def remover():
    opcao = 0
    if not lista:
        print("Sua lista está vazia!")

    else:
        while opcao == 0:
         opcao = int(input("Deseja remover o ultimo item da lista?(1-Sim) (2-Não)"))

        if opcao == 1:
            lista.pop()
            print("Você removeu um item!")
            opcao = 0
        else:
            print("Você removeu nenhum item!") 
            opcao = 1

def mostrar():
    opcao = 0

    while opcao == 0:
        opcao = int(input("Qual tipo de lista você deseja? (1- Atual) (2- Historico) (3- Voltar)"))
        if opcao == 1:
            print("Essa é a lista atual:")
            print(lista)
        else:
            if opcao == 2:
              print("Essa é a lista de historico:")
              print(historico)
            else:
                print("Estamos lhe retornando...")
                break

escolha = 0

while True:
    print("Seja bem vindo! A Lista de Desejos! \n Fique a vontade para organizar sua lista de seu jeito.")
    escolha = int(input("Escolha entre um dessas opções: \n 1 - (Adicionar item)\n 2 - (Remover item)\n 3 - (Mostrar listas)\n 4 - (Sair da aplicação)\n \n Digite aqui em baixo:\n"))
    if escolha == 1:
        adicionar()
    else: 
        if escolha == 2:
            remover()
        else:
            if escolha == 3:
                mostrar()
            else:
                if escolha == 4:
                    break
                else:
                    print("Opção invalida, por favor, tente novamente.")