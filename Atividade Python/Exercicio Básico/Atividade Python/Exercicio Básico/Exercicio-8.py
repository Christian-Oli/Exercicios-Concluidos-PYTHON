contatos = {
   
}

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



print(contatos)
adicionar()
print(contatos)
remover()
print(contatos)