# Variaveis do tipo Lista
lista = []
historico = []

# Função para ser chamada no menu: Adicionar
def adicionar():
    # Variavel "Local" usada na escolha
    opcao = 0
    # Laço While
    while opcao == 0:
        # Input que vai levar a usuario ao seu destino.
        item = input("Digite aqui o item que deseja em sua lista de desejos:\n")
        # Input que vai pergunta ao usuario se ele realmente deseja fazer a ação.
        opcao = int(input("Tem certeza em adicionar esse item? (1-Sim) (2-Não)"))
        # If sobre as escolhas
        if opcao == 1:
            # Caso for 1 irá printar, adicionar e registrar na lista de historico.
            print(f"Você adicionou o item: {item}!")
            lista.append(item)
            historico.append(item)
        else:
            # caso for outro valor o irá printar, e resetar as variaveis.
            print(f"Você não adicionou: {item}")
            item = ""
            opcao = 0
            continue

# Função para ser chamada no menu: remover
def remover():
    # Variavel "Local" usada na escolha
    opcao = 0
    # If para saber se a lista está vazia ou não, caso contrario irá printar o alerta
    if not lista:
        print("Sua lista está vazia!")
    # Caso tiver algum item irá avançar.
    else:
        # Irá levar o usuario a escolha usando a variavel opção como parametro
        while opcao == 0:
         opcao = int(input("Deseja remover o ultimo item da lista?(1-Sim) (2-Não)"))
        # Caso a variavel for verdadeira, irá executar o comando Pop (remover o ultimo item adicionado)
        if opcao == 1:
            lista.pop()
            # Printar o alerta
            print("Você removeu um item!")
            # resetar a variavel
            opcao = 0
        else:
            #Irá printar o alerta caso o opção for outro valor
            print("Você removeu nenhum item!") 
            opcao = 1

# Função para ser chamada no menu: mostrar
def mostrar():
    # Variavel "Local" usada na escolha
    opcao = 0
    # Irá levar o usuario a escolha usando a variavel opção como parametro
    while opcao == 0:
        # Input que vai levar a usuario ao seu destino.
        opcao = int(input("Qual tipo de lista você deseja? (1- Atual) (2- Historico) (3- Voltar)"))
        # Input que vai pergunta ao usuario se ele realmente deseja fazer a ação.
        if opcao == 1:
            # caso a opção digitada for 1, irá printar a lista atual com o alerta juntamente da lista em si.
            print("Essa é a lista atual:")
            print(lista)
        else:
            if opcao == 2:
              # caso a opção digitada for 1, irá printar o historico com o alerta juntamente da lista em si.
              print("Essa é a lista de historico:")
              print(historico)
            else:
                # caso nenhum das opções, irá printar o alerta e fechar a função 
                print("Estamos lhe retornando...")
                break

# variavel de escolha do menu principal
escolha = 0
# While reponsavel pelo loop total do programa.
while True:
    # Saudações
    print("Seja bem vindo! A Lista de Desejos! \n Fique a vontade para organizar sua lista de seu jeito.")
    # Input responsavel por toda interface do menu de escolha.
    escolha = int(input("Escolha entre um dessas opções: \n 1 - (Adicionar item)\n 2 - (Remover item)\n 3 - (Mostrar listas)\n 4 - (Sair da aplicação)\n \n Digite aqui em baixo:\n"))
    # If responsavel pelo controle de ações com a variavel escolha
    if escolha == 1:
        # chamado da função
        adicionar()
    else: 
        if escolha == 2:
            # chamado da função
            remover()
        else:
            if escolha == 3:
                # chamado da função
                mostrar()
            else:
                if escolha == 4:
                    # Quebra da aplicação
                    break
                else:
                    # Alerta de escolha diferente.
                    print("Opção invalida, por favor, tente novamente.")