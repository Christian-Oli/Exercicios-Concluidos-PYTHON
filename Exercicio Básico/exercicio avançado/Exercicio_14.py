# Variavel responsavel por armazenar o CPF digitado pelo usuario
cpf_base = ""

# Recebe o CPF e remove pontos e traços para facilitar os calculos
cpf_base = input("|Digite aqui seu CPF(limite de 11 caracteres):").replace(".", "").replace("-", "")

# Verifica se o CPF possui exatamente 11 caracteres
if len(cpf_base) != 11:
        print("|CPF passou dos limite de caracteres.|")

# Variavel utilizada para percorrer os numeros do CPF
i = 0

# Lista responsavel por armazenar os calculos do primeiro digito verificador
calculado_d1 = []

# Variavel utilizada para armazenar o resultado temporario
resultado_d1 = ""

# Laço responsavel pelos calculos do primeiro digito verificador
for numero in range(10, 1, -1):

        # Captura o numero atual do CPF
        dominante = int(cpf_base[i])

        # Multiplica pelo peso correspondente
        resultado_d1 = numero * dominante

        # Adiciona o resultado na lista
        calculado_d1.append(resultado_d1)

        # Avança para o proximo numero do CPF
        i = 1 + i

# Soma todos os resultados do primeiro calculo
soma_d1 = calculado_d1[0] + calculado_d1[1] + calculado_d1[2] + calculado_d1[3] + calculado_d1[4] + calculado_d1[5] + calculado_d1[6] + calculado_d1[7] + calculado_d1[8]

# Obtém o resto da divisão por 11
resto_d1 = soma_d1 % 11

# Verifica qual deve ser o primeiro digito verificador
if resto_d1 <= 1:
        digito_1 = 0
else:
        digito_1 = 11 - resto_d1

# Variavel utilizada para percorrer os numeros do CPF novamente
y = 0

# Lista responsavel por armazenar os calculos do segundo digito verificador
calculado_d2 = []

# Variavel utilizada para armazenar resultados temporarios
resultado_d2 = ""

# Laço responsavel pelos calculos do segundo digito verificador
for numero2 in range(11, 1, -1):

        # Captura o numero atual do CPF
        dominante = int(cpf_base[y])

        # Multiplica pelo peso correspondente
        resultado_d2 = numero2 * dominante

        # Adiciona o resultado na lista
        calculado_d2.append(resultado_d2)

        # Avança para o proximo numero
        y = 1 + y

# Soma todos os resultados do segundo calculo
soma_d2 = calculado_d2[0] + calculado_d2[1] + calculado_d2[2] + calculado_d2[3] + calculado_d2[4] + calculado_d2[5] + calculado_d2[6] + calculado_d2[7] + calculado_d2[8] + calculado_d2[9]

# Obtém o resto da divisão por 11
resto_d2 = soma_d2 % 11

# Verifica qual deve ser o segundo digito verificador
if resto_d2 <= 1:
        digito_2 = 0
else:
        digito_2 = 11 - resto_d2

# Exibe o CPF informado
print(cpf_base)

# Exibe os digitos calculados
print(digito_1)
print(digito_2)

# Verifica se o primeiro digito calculado é igual ao do CPF
if digito_1 == int(cpf_base[9]):

        print("Seu primeiro digito é válido.")

        # Verifica se o segundo digito calculado é igual ao do CPF
        if digito_2 == int(cpf_base[10]):

                print("Seu segundo digito é válido.")
                print("Seu CPF está confirmado! Parabéns.")

        else:

               print("Seu segundo digito é invalido, LOGO, seu cpf é inválido.")

else:

        print("Seu primeiro digito é invalido, LOGO, seu cpf é inválido.")