# Classe responsavel por representar uma conta bancaria
class ContaBancaria:

    # Construtor responsavel por criar uma nova conta
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.saldo = 0
        self.titular = titular

    # Metodo responsavel por adicionar dinheiro ao saldo
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado.")

    # Metodo responsavel por sacar dinheiro da conta
    def sacar(self, valor):

        # Verifica se existe saldo suficiente para o saque
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")

        else:
            print("Saldo insuficiente.")

    # Metodo responsavel por exibir o saldo atual
    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


# Classe responsavel por representar um cliente do banco
class Cliente:

    # Construtor responsavel por armazenar os dados do cliente
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

        # Lista responsavel por armazenar as contas do cliente
        self.contas = []

    # Metodo responsavel por adicionar uma conta ao cliente
    def adicionar_conta(self, conta):
        self.contas.append(conta)


# Classe responsavel por gerenciar os clientes e contas
class Banco:

    # Construtor responsavel por armazenar todos os clientes
    def __init__(self):
        self.clientes = []

    # Metodo responsavel por adicionar um novo cliente ao banco
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Metodo responsavel por procurar uma conta pelo numero
    def buscar_conta(self, numero_conta):

        # Percorre todos os clientes cadastrados
        for cliente in self.clientes:

            # Percorre todas as contas do cliente atual
            for conta in cliente.contas:

                # Verifica se encontrou a conta desejada
                if conta.numero_conta == numero_conta:
                    return conta

        # Retorna None caso a conta não exista
        return None


# Criação do objeto banco
banco = Banco()

# Criação de um cliente
cliente1 = Cliente("Vagner Professor", "111.111.111-00")

# Criação de uma conta bancaria
conta1 = ContaBancaria(1001, cliente1.nome)

# Adiciona a conta ao cliente
cliente1.adicionar_conta(conta1)

# Adiciona o cliente ao banco
banco.adicionar_cliente(cliente1)

# Realiza um deposito
conta1.depositar(1000)

# Realiza um saque
conta1.sacar(300)

# Exibe o saldo atual
conta1.verificar_saldo()

# Procura uma conta pelo numero informado
conta_encontrada = banco.buscar_conta(1001)

# Verifica se a conta foi encontrada
if conta_encontrada:

    print("conta existente!")

    # Exibe o saldo da conta encontrada
    conta_encontrada.verificar_saldo()