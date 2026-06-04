# Classe responsavel por armazenar a palavra secreta do jogo
class Palavra:

    # Construtor responsavel por receber a palavra escolhida
    def __init__(self, palavra):

        # Converte a palavra para maiusculo para facilitar as comparações
        self.palavra = palavra.upper()

    # Metodo responsavel por mostrar o progresso atual da palavra
    def mostrar_progresso(self, letras_acertadas):

        # Variavel utilizada para montar a exibição da palavra
        resultado = ""

        # Percorre todas as letras da palavra
        for letra in self.palavra:

            # Verifica se a letra ja foi descoberta pelo jogador
            if letra in letras_acertadas:

                # Exibe a letra encontrada
                resultado += letra + " "

            else:

                # Exibe um espaço oculto para letras não descobertas
                resultado += "_ "

        return resultado


# Classe responsavel por representar o jogador
class Jogador:

    # Construtor responsavel por definir as tentativas e letras utilizadas
    def __init__(self):

        # Quantidade inicial de tentativas
        self.tentativas = 6

        # Lista responsavel por armazenar as letras digitadas
        self.letras_usadas = []

    # Metodo responsavel por receber uma letra do usuario
    def adivinhar_letra(self):

        # Captura a letra digitada
        letra = input("Digite uma letra: ").upper()

        # Armazena a letra na lista de tentativas
        self.letras_usadas.append(letra)

        return letra


# Classe principal responsavel pelo funcionamento do jogo
class Jogo:

    # Construtor responsavel por criar a palavra e o jogador
    def __init__(self, palavra):

        # Cria o objeto Palavra
        self.palavra = Palavra(palavra)

        # Cria o objeto Jogador
        self.jogador = Jogador()

    # Metodo responsavel por iniciar a partida
    def iniciar(self):

        # Enquanto ainda houver tentativas disponiveis
        while self.jogador.tentativas > 0:

            # Exibe o estado atual da palavra
            print("\nPalavra:")

            print(
                self.palavra.mostrar_progresso(
                    self.jogador.letras_usadas
                )
            )

            # Recebe a letra digitada pelo jogador
            letra = self.jogador.adivinhar_letra()

            # Verifica se a letra não existe na palavra
            if letra not in self.palavra.palavra:

                # Remove uma tentativa
                self.jogador.tentativas -= 1

                # Exibe mensagens de erro
                print("Letra incorreta!")

                print(
                    f"Tentativas restantes: {self.jogador.tentativas}"
                )

            # Variavel utilizada para verificar a vitória
            venceu = True

            # Percorre todas as letras da palavra
            for caractere in self.palavra.palavra:

                # Verifica se ainda existe letra não descoberta
                if caractere not in self.jogador.letras_usadas:

                    venceu = False

            # Caso todas as letras tenham sido descobertas
            if venceu:

                print("\nParabéns! Você venceu!")
                print("Palavra:", self.palavra.palavra)

                # Encerra o jogo
                return

        # Executado quando o jogador perde todas as tentativas
        print("\nGame Over!")
        print("A palavra era:", self.palavra.palavra)


# Criação do jogo com a palavra escolhida
jogo = Jogo("Vagner")

# Inicia a partida
jogo.iniciar()