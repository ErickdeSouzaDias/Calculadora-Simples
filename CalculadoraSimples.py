# Area de funcoes

def cabecalho(): # Procedimento de exibicao do cabecalho do procedimento.
    print(50*'=')
    print('\t\t\t\tCalculadora Simples')
    print(50*'=')

def limpaTela(): # Procedimento para limpar a tela do usuario
    print(25*'\n')

def escolhaFunc():
    print('Qual operacao deve ser realizada: ')
    print('1 - Soma\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao')
    opcao = int(input('Sua opcao: '))
# ---------------------------------------------------

# Area de variaveis globais

parada = 0

# Programa principal

cabecalho() # Solicita a exibicao do cabecalho da funcao

while (parada != 1):
    n = float(input('Informe o primeiro valor: '))
    escolhaFunc()
# ---------------------------------------------------