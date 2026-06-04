import requests
from bs4 import BeautifulSoup

# Variavel contendo o endereço do site que sera acessado
url = "https://g1.globo.com/"

# Realiza a requisição para o site
resposta = requests.get(url)

# Verifica se o acesso ao site foi realizado com sucesso
if resposta.status_code == 200:

    # Converte o HTML da pagina para um objeto BeautifulSoup
    soup = BeautifulSoup(resposta.text, "html.parser")

    # Conjunto responsavel por armazenar os titulos sem repetição
    titulos = set()

    # Procura todas as tags h2 presentes na pagina
    for titulo in soup.find_all("h2"):

        # Remove espaços extras do texto encontrado
        texto = titulo.get_text().strip()

        # Verifica se o texto não está vazio
        if texto:

            # Adiciona o titulo encontrado ao conjunto
            titulos.add(texto)

    # Cria ou sobrescreve o arquivo de noticias
    with open(r"Exercicio Desafio\Exercicio_19\noticias.txt", "w", encoding="utf-8") as arquivo:

        # Percorre todos os titulos encontrados
        for titulo in titulos:

            # Escreve cada titulo em uma nova linha do arquivo
            arquivo.write(titulo + "\n")

    # Alerta informando que o processo foi concluido
    print("Títulos salvos em noticias.txt")

else:

    # Alerta caso o site não possa ser acessado
    print("Erro ao acessar o site.")