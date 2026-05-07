contatos = []

def adicionar():
    nome = input("Adicione o nome do contato aqui:")
    idade = input("Adicione um numero")
    telefone = input("Adicione o numero do contato aqui:")
    email = input("Adicione o email do contato aqui:")

    n_contato = {"nome": nome, "idade": idade, "telefone": telefone, "email": email}
    contatos.append(n_contato)

print(contatos)
adicionar()
print(contatos)