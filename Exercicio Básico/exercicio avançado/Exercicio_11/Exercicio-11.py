# Bloco Try responsavel por tentar abrir e ler o arquivo
try:

    # Abre o arquivo em modo de leitura utilizando UTF-8
    with open(r"exercicio avançado\Exercicio_11\banco.txt", "r", encoding="utf-8") as arquivo:

        # Armazena todo o conteudo do arquivo na variavel mostrar
        mostrar = arquivo.read()

        # Exibe o conteudo do arquivo na tela
        print(mostrar)

# Caso o arquivo não exista ou o caminho esteja incorreto
except FileNotFoundError:

        # Alerta informando que o arquivo não foi encontrado
        print("Arquivo não foi encontrado ou inexistente.")

        # Sugere verificar o nome ou local do arquivo
        print("Verifique o formato do arquivo ou o nome no diretorio")

# Captura qualquer outro erro que possa acontecer
except Exception as e:

        # Exibe uma mensagem junto com o erro encontrado
        print(f"Alguma coisa deu muito errado. {e}")