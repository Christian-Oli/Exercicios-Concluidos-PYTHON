# Dicionario responsavel por armazenar todos os contatos
contatos = {}

# Função para ser chamada no menu: Adicionar contato
def adicionar():

    # Inputs responsaveis por coletar os dados do contato
    nome = input("Adicione o nome do contato aqui:")
    idade = input("Adicione um numero")
    telefone = input("Adicione o numero do contato aqui:")
    email = input("Adicione o email do contato aqui:")
    id = input("Adicione uma chave para esse contato:")

    # Adiciona um novo contato ao dicionario usando o id como chave
    contatos[id] = {"nome": nome, "idade": idade, "telefone": telefone, "email": email}

# Função para ser chamada no menu: Remover contato
def remover():

    # Laço responsavel por pedir o id até encontrar um contato valido
    while True:

     # Input que recebe o id do contato que sera removido
     contato_del = input("Digite aqui o id do contato:")

     # Verifica se o id informado existe no dicionario
     if contato_del in contatos:

        # Remove o contato encontrado
        del contatos[contato_del]

        # Encerra o laço
        break

     else:

        # Alerta caso o contato não exista
        print("Esse contato não existe.")

        # Retorna ao inicio do laço
        continue

# Função para ser chamada no menu: Mostrar contatos
def mostrar():

   # Verifica se existe algum contato cadastrado
   if not contatos:

      # Alerta caso a lista esteja vazia
      print("A lista de contatos está vazia! Tente novamente.")

   else:

      # Exibe todos os contatos cadastrados
      print(contatos)

# Variavel responsavel pela escolha do menu principal
escolha = 0

# Laço principal da aplicação
while True:

    # Titulo e opções do menu
    print("Aplicação de contatos")
    print("(1)- Adicionar Contato (2)- Remover (3)- Mostrar (4)- sair")

    # Input responsavel pela escolha da ação
    escolha = int(input("Escolha uma dessas opções:"))

    # Controle das opções do menu
    if escolha == 1:

        # Chama a função adicionar
        adicionar()

    else:

        if escolha == 2:

            # Chama a função remover
            remover()

        else:

            if escolha == 3:

                # Chama a função mostrar
                mostrar()

            else:

                if escolha == 4:

                    # Encerra a aplicação
                    break

                else:

                    # Alerta caso o usuario digite uma opção invalida
                    print("Opção invalida, por favor, tente novamente.")