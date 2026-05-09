contatos = {}

def adicionar():
    
    nome = input("Adicione o nome do contato aqui:")
    idade = input("Adicione um numero")
    telefone = input("Adicione o numero do contato aqui:")
    email = input("Adicione o email do contato aqui:")
    id = input("Adicione uma chave para esse contato:")

    contatos[id] = {"nome": nome, "idade": idade, "telefone": telefone, "email": email}

def remover():
    while True:
     contato_del = input("Digite aqui o id do contato:")
     if contato_del in contatos:
        del contatos[contato_del]
        break
     else:
        print("Esse contato não existe.")
        continue

def mostrar():
   if not contatos:
      print("A lista de contatos está vazia! Tente novamente.")
   else:
      print(contatos)


escolha = 0

while True:
    print("Aplicação de contatos")
    print("(1)- Adicionar Contato (2)- Remover (3)- Mostrar (4)- sair")
    escolha = int(input("Escolha uma dessas opções:"))
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