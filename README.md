# PROJETO PYTHON: Conversor de valor Real em Hexadecimal usando o Padrão IEEE754
> Programa que recebe um valor Real e Converte no Padrão IEEE754.

O programa deve receber um valor decimal qualquer e converter para o valor Hexadecimal no 
padrão Computacional IEEE754, passando por todos os processos de conversão sem o uso de Bibliotecas para
32 e 64 Bits.

- Receber o valor Real;
- Separar Inteiro de Decimal;
- Converter cada parte em Binário;
- Juntar essas partes Binárias;
- Normalizar;
- Descobrir o valor do Expoente da Normalização;
- Somar o Expoente com o valor do Bias;
- Converter o Valor do expoente em Binário;
- Separar a Mantissa o Expoente o o Valor  de Bit;
- Converter o Binário em Hexadecimal.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

# Exemplo de Uso
### Classe
```
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
        self.valor_expoente_32_decimal = 0
        self.valor_expoente_64 = 0
        self.padrao_32 = []
        self.padrao_64 = []
        self.separador_32 = []
        self.separador_64 = []
        self.valores_decimais_32 = []
        self.valores_decimais_64 = []
        self.hexadecimal_32 = ''
        self.hexadecimal_64 = ''
```
![Classe](https://github.com/ThiagoLozano/Conversor-IEEE754/blob/main/Screenshot/Classe.PNG)

### Recebe valor Real
```
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
```
![Valor Real](https://github.com/ThiagoLozano/Conversor-IEEE754/blob/main/Screenshot/Recebe_Valor.PNG)
