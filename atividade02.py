# Integrandes: Thiago Lozano, AlexSandro Castro, Glauco Conceição, Enzo Eolo Borsatti.
# RAs: 20219833|18110791|20118948|17111571
# Laboratório e Organização Computacional
# Ano: 2020
class ConversorIEEE754:
    # Método Construtor.
    def __init__(self):
        self.valor_real = 0
        self.part_int_bin_32 = []
        self.part_float_bin_32 = []
        self.part_float_bin_64 = []
        self.juncao_32 = []
        self.juncao_64 = []
        self.normalizar_32 = []
        self.normalizar_64 = []
        self.valor_expoente_32 = 0
        self.valor_expoente_64 = 0
        self.padrao_32 = []
        self.padrao_64 = []
        self.separador_32 = []
        self.separador_64 = []
        self.valores_decimais_32 = []
        self.valores_decimais_64 = []
        self.hexadecimal_32 = ''
        self.hexadecimal_64 = ''

    # Receber um valor Real qualquer.
    def Set_Valor(self):
        # Valida o tipo de dado que for digitado.
        while True:
            try:
                # Pega o valor real digitado.
                self.valor_real = float(input("Digite um valor Real: "))
                self.Parte_Inteira()
                break
            except ValueError:
                print("Erro: Tipo de Dado inválido\n")

    # Converte a parte Inteira para Binário.
    def Parte_Inteira(self):

        # Pega apenas a parte inteira do valor.
        inteiro = int(self.valor_real)

        # Caso o valor real seja negativo
        if self.valor_real < 0:
            inteiro = inteiro * -1

        # Converte para Binário.
        resto = []
        quociente = []

        while True:
            # Faz a divisão até não poder mais.
            quociente.append(inteiro // 2)
            resto.append(int(inteiro % 2))
            inteiro = inteiro // 2

            # Pega o último valor do Quociente e coloca na lista de Restos.
            if inteiro < 2:
                ultimo = len(quociente) - 1
                resto.append(quociente[ultimo])
                break

        # Lê o resto das divisões de trás para frente e atribui o valor binário a variável.
        self.part_int_bin_32 = resto[::-1]

        # Chama as função.
        self.Parte_Decimal_32()
        self.Parte_Decimal_64()

    # Converte a parte Decimal para Binário 32 Bits.
    def Parte_Decimal_32(self):

        # Pega apenas a parte decimal do valor.
        if self.valor_real < 0:
            # Caso o valor Real seja negativo.
            decimal = abs(self.valor_real) - int(abs(self.valor_real))
        else:
            # Caso o valor Real seja Positivo.
            decimal = self.valor_real - int(self.valor_real)

        # Faz as multiplicações sucessivas até gerar os valores binários para 32 bits.
        binario = []
        for c in range(19):
            decimal * 2
            if int(decimal) == 1:
                decimal = decimal - 1
            decimal = decimal * 2
            binario.append(int(decimal))

        # Atribui o valor binário a variável.
        self.part_float_bin_32 = binario

        # Chama a função.
        self.Juntar_Partes_32()

    # Converte a parte Decimal para Binário 64 Bits.
    def Parte_Decimal_64(self):

        # Pega apenas a parte decimal do valor.
        if self.valor_real < 0:
            # Caso o valor Real seja negativo.
            decimal = abs(self.valor_real) - int(abs(self.valor_real))
        else:
            # Caso o valor Real seja Positivo.
            decimal = self.valor_real - int(self.valor_real)

        # Faz as multiplicações sucessivas até gerar os valores binários para 32 bits.
        binario = []
        for c in range(48):
            decimal * 2
            if int(decimal) == 1:
                decimal = decimal - 1
            decimal = decimal * 2
            binario.append(int(decimal))

        # Atribui o valor binário a variável.
        self.part_float_bin_64 = binario

        # Chama a função.
        self.Juntar_Partes_64()

    # Junta a parte Inteira Binário com a parte Float Binário 32 Bits.
    def Juntar_Partes_32(self):

        # Acrescenta uma vírgula (.) par separar Inteiro do Float.
        self.part_int_bin_32.append('.')

        # Concatena as duas partes.
        self.juncao_32 = self.part_int_bin_32 + self.part_float_bin_32

        # Chama a função.
        self.Normalizar_32()

    # Junta a parte Inteira Binário com a parte Float Binário 64 Bits.
    def Juntar_Partes_64(self):

        # Concatena as duas partes.
        self.juncao_64 = self.part_int_bin_32 + self.part_float_bin_64

        # Chama a função.
        self.Normalizar_64()

    # Normaliza o valor Binário da junção 32 Bits.
    def Normalizar_32(self):

        # Atribui o valor para normalizar.
        self.normalizar_32 = self.juncao_32

        # Busca a posição na vírgula.
        for c in self.normalizar_32:
            if c == '.':
                self.valor_expoente_32 = self.normalizar_32.index(c)  # Pega a posição do (.) que separa os valores.

        self.normalizar_32.remove('.')  # Remove a vírgula da posição atual.
        self.normalizar_32.insert(1,
                                  '.')  # Coloca a vírgula na posição '1' que separa INT do FLOAT em uma casa decimal.

        self.valor_expoente_32 = self.valor_expoente_32 - 1  # Encontra o valor do expoente na normalização.

        # Chama a função.
        self.Bias_32()

    # Normaliza o valor Binário da junção 64 Bits.
    def Normalizar_64(self):

        # Atribui o valor para normalizar.
        self.normalizar_64 = self.juncao_64

        # Busca a posição na vírgula.
        for c in self.normalizar_64:
            if c == '.':
                self.valor_expoente_64 = self.normalizar_64.index(c)  # Pega a posição do (.) que separa os valores.

        self.normalizar_64.remove('.')  # Remove a vírgula da posição atual.
        self.normalizar_64.insert(1,
                                  '.')  # Coloca a vírgula na posição '1' que separa INT do FLOAT em uma casa decimal.

        self.valor_expoente_64 = self.valor_expoente_64 - 1  # Encontra o valor do expoente na normalização.

        # Chama a função.
        self.Bias_64()

    # Converte o expoente para Binário 32 Bits.
    def Bias_32(self):

        # Valor padrão para 8bits do expoente.
        bias_8_bits = 127

        soma = self.valor_expoente_32 + bias_8_bits

        # Converte o valor da soma em Binário.
        resto = []
        quociente = []

        while True:
            # Coloca o Resto e o Quociente nas listas correspondentes.
            quociente.append(soma // 2)
            resto.append(int(soma % 2))
            soma = soma // 2

            # Pega o último valor do Quociente e coloca na lista de Restos.
            if soma < 2:
                ultimo = len(quociente) - 1
                resto.append(quociente[ultimo])
                break

        # Atribui o valor binário na variável.
        self.valor_expoente_32 = resto[::-1]

        # Chama a função.
        self.Padrao_32_Bits()

    # Converte o expoente para Binário 64 Bits.
    def Bias_64(self):

        # Valor padrão para 8bits do expoente.
        bias_11_bits = 1023

        soma = self.valor_expoente_64 + bias_11_bits

        # Converte o valor da soma em Binário.
        resto = []
        quociente = []

        while True:
            # Coloca o Resto e o Quociente nas listas correspondentes.
            quociente.append(soma // 2)
            resto.append(int(soma % 2))
            soma = soma // 2

            # Pega o último valor do Quociente e coloca na lista de Restos.
            if soma < 2:
                ultimo = len(quociente) - 1
                resto.append(quociente[ultimo])
                break

        # Atribui o valor binário na variável.
        self.valor_expoente_64 = resto[::-1]

        # Chama a função.
        self.Padrao_64_Bits()

    # Retorna o valor no padrão 32 bits.
    def Padrao_32_Bits(self):

        # Apaga os valores antes da vírgula e a vírgula.
        del self.juncao_32[0]
        del self.juncao_32[0]

        # Atribui os valores as variáveis.
        expoente = self.valor_expoente_32
        mantissa = self.juncao_32

        # Verifica se o valor é Positivo ou Negativo.
        if self.valor_real > 0:
            # Primeiro valor é 0.
            self.padrao_32.insert(0, 0)
        else:
            # Primeiro valor é 1.
            self.padrao_32.insert(0, 1)

        # Insere o valor do expoente.
        for c in expoente:
            self.padrao_32.append(c)

        # Insere o valor da mantissa.
        for c in mantissa:
            self.padrao_32.append(c)

        # Chama a função.
        self.Separador_32()

    # Retorna o valor no padrão 64 bits.
    def Padrao_64_Bits(self):

        # Apaga os valores antes da vírgula e a vírgula.
        del self.juncao_64[0]
        del self.juncao_64[0]

        # Atribui os valores as variáveis.
        expoente = self.valor_expoente_64
        mantissa = self.juncao_64

        # Verifica se o valor é Positivo ou Negativo.
        if self.valor_real > 0:
            # Primeiro valor é 0.
            self.padrao_64.insert(0, 0)
        else:
            # Primeiro valor é 1.
            self.padrao_64.insert(0, 1)

        # Insere o valor do expoente.
        for c in expoente:
            self.padrao_64.append(c)

        # Insere o valor da mantissa.
        for c in mantissa:
            self.padrao_64.append(c)

        # Chama a função.
        self.Separador_64()

    # Separa o valor Binários em SubBlocos de 4 bits, 32 Bits.
    def Separador_32(self):

        # Laço que separa os blocos com 4 bits cada.
        for i in range(0, len(self.padrao_32), 4):
            self.separador_32.append(self.padrao_32[i:i + 4])

        # Chama a função.
        self.Binario_para_Decimal_32()

    # Separa o valor Binários em SubBlocos de 4 bits, 64 Bits.
    def Separador_64(self):

        # Laço que separa os blocos com 4 bits cada.
        for i in range(0, len(self.padrao_64), 4):
            self.separador_64.append(self.padrao_64[i:i + 4])

        # Chama a função.
        self.Binario_para_Decimal_64()

    # Converte o valor Binário  para Hexadecimal 32 Bits.
    def Binario_para_Decimal_32(self):

        contador = 0  # Contador de Blocos.
        valor_convertido = []  # Lista para armazenar a conversão para decimal.
        valores_separados = []  # Lista para separar os valores decimais um do outro.
        self.valores_decimais_32 = []  # Lista com a soma valores decimais separados.

        # Faz a contagem de blocos.
        for c in self.separador_32:
            contador += 1

        # Laço para converter os valores binários em decimal.
        for c in range(contador):
            for i, v in enumerate(self.separador_32[c][::-1]):
                valor_convertido.append((2 ** i) * v)

        # Laço para separar os valor decimais de cada bloco.
        for i in range(0, len(valor_convertido), 4):
            valores_separados.append(valor_convertido[i:i + 4])

        # Laço para somar os valores decimais de cada bloco.
        for c in valores_separados:
            self.valores_decimais_32.append(sum(c))

        # Chama a função.
        self.Decimal_para_Hexadecimal_32()

    # Converte o valor Binário  para Hexadecimal 64 Bits.
    def Binario_para_Decimal_64(self):

        contador = 0  # Contador de Blocos.
        valor_convertido = []  # Lista para armazenar a conversão para decimal.
        valores_separados = []  # Lista para separar os valores decimais um do outro.
        self.valores_decimais_64 = []  # Lista com a soma valores decimais separados.

        # Faz a contagem de blocos.
        for c in self.separador_64:
            contador += 1

        # Laço para converter os valores binários em decimal.
        for c in range(contador):
            for i, v in enumerate(self.separador_64[c][::-1]):
                valor_convertido.append((2 ** i) * v)

        # Laço para separar os valor decimais de cada bloco.
        for i in range(0, len(valor_convertido), 4):
            valores_separados.append(valor_convertido[i:i + 4])

        # Laço para somar os valores decimais de cada bloco.
        for c in valores_separados:
            self.valores_decimais_64.append(sum(c))

        # Chama a função.
        self.Decimal_para_Hexadecimal_64()

    # Converte o valor Decimal para Hexadecimal 32 Bits.
    def Decimal_para_Hexadecimal_32(self):

        # Atribui a lista de decimais em uma variável.
        decimal = self.valores_decimais_32

        separa_valores = []  # Lista para separar os valores em blocos.
        apenas_valores = []  # Lista com só os valores da conversão.

        # Converte em Hexadecimal.
        lista = list(map(lambda x: hex(x), decimal))

        # Separa os valores em blocos.
        for c in lista:
            separa_valores += c

        # Tira o 'x' e o '0' do Hexadecimal.
        for c in separa_valores:
            if c != 'x' and c != '0':
                apenas_valores.append(c)

        # Coloca tudo em uma String.
        for c in apenas_valores:
            self.hexadecimal_32 += c.upper()

    # Converte o valor Decimal para Hexadecimal 64 Bits.
    def Decimal_para_Hexadecimal_64(self):

        # Atribui a lista de decimais em uma variável.
        decimal = self.valores_decimais_64

        separa_valores = []  # Lista para separar os valores em blocos.
        apenas_valores = []  # Lista com só os valores da conversão.

        # Converte em Hexadecimal.
        lista = list(map(lambda x: hex(x), decimal))

        # Separa os valores em blocos.
        for c in lista:
            separa_valores += c

        # Tira o 'x' e o '0' do Hexadecimal.
        for c in separa_valores:
            if c != 'x' and c != '0':
                apenas_valores.append(c)

        # Coloca tudo em uma String.
        for c in apenas_valores:
            self.hexadecimal_64 += c.upper()

    # Resultado.
    def Resultado(self):
        print('\n32 Bits: {}'.format(self.hexadecimal_32))
        print('64 Bits: {}'.format(self.hexadecimal_64))


usuario = ConversorIEEE754()
usuario.Set_Valor()
usuario.Resultado()
