# Importa a biblioteca responsavel por trabalhar com datas e horarios
from datetime import datetime

# Variavel utilizada para armazenar o item digitado pelo usuario
item = ""

# Bloco Try responsavel por tentar registrar um novo item no carrinho
try:

    # Abre o arquivo do carrinho em modo de adição
    with open(r"exercicio avançado\Exercicio_13\carrinho.txt", "a", encoding="utf-8") as carrinho:

        # Recebe o item que sera registrado
        item = input("Digite aqui o item que deseja registrar:\n")

        # Captura a data e hora atual do sistema
        date_atual = datetime.now()

        # Formata a data para um formato mais amigavel
        date_formulation = date_atual.strftime("|Data: %d/%m/%Y | Horas: %H:%M:%S |")

        # Registra o item juntamente da data e hora
        carrinho.write(f"{date_formulation} | {item} foi adicionado com sucesso ao carrinho.\n")

        # Alerta informando que o item foi registrado
        print(f"{item} carrinho foi adicionado com sucesso.")

        # Abre o arquivo de log para registrar a ação realizada
        with open(r"exercicio avançado\Exercicio_13\logregister.txt", "a", encoding="utf-8") as log_register:

            # Registra uma informação de sucesso no arquivo de log
            log_register.write(f"{date_formulation} |TYPE INFO| O item: ''{item}'' foi adicionado.\n")

# Caso o arquivo do carrinho não seja encontrado
except FileNotFoundError:

    # Abre o arquivo de log para registrar o erro
    with open(r"exercicio avançado\Exercicio_13\logregister.txt", "a", encoding="utf-8") as log_register:

        # Captura a data e hora atual
        date_atual = datetime.now()

        # Formata a data para registro
        date_formulation = date_atual.strftime("|Data: %d/%m/%Y | Horas: %H:%M:%S |")

        # Registra um aviso no arquivo de log
        log_register.write(f"{date_formulation} |TYPE WARNING| O arquivo ''carrinho'' não foi encontrado em seu diretorio.\n")

        # Exibe o alerta ao usuario
        print("Ocorreu um imprévisto: Arquivo vinculado inexistente...")

# Captura qualquer outro erro inesperado
except Exception as e:

    # Abre o arquivo de log para registrar o erro
    with open(r"exercicio avançado\Exercicio_13\logregister.txt", "a", encoding="utf-8") as log_register:

        # Captura a data e hora atual
        date_atual = datetime.now()

        # Formata a data para registro
        date_formulation = date_atual.strftime("|Data: %d/%m/%Y | Horas: %H:%M:%S |")

        # Registra um erro inesperado no arquivo de log
        log_register.write(f"{date_formulation} |TYPE ERROR| Um erro inesperado aconteceu.\n")