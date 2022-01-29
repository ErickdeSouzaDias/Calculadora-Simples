# Area de funcoes

def cabecalho(): # Procedimento de exibicao do cabecalho do procedimento.
    print(50*'=')
    print('\t\t\t\tCalculadora Simples')
    print(50*'=')

def limpaTela(): # Procedimento para limpar a tela do usuario
    print(25*'\n')

def escolhaFunc(): # Procedimento o qual exibe a lista de operações suportadas
    print('Qual operacao deve ser realizada: ')
    print('1 - Soma\n2 - Subtracao\n3 - Multiplicacao\n4 - Divisao\n5 - Sair')
    opcao = int(input('Sua opcao: '))
    return opcao

def Soma(x = 0, y = 0): # Operação de Adição
    print(f'{x} somando {y} é {x+y}.')

def Subtracao(x = 0, y = 0): # Operacao de Subtraçao
    print(f'{x} subtraindo {y} é {x-y}.')

def Multiplicacao(x = 0, y = 0): # Operação de Multiplicação
    print(f'A multiplicação de {x} por {y} é {x*y}.')

def Divisao(x = 0, y = 0): # Operação de divisão
    print(f'A divisão de {x} por {y} é {x/y}.')

# ---------------------------------------------------

# Area de variaveis globais

parada = 0

# Programa principal

cabecalho() # Solicita a exibicao do cabecalho da funcao

while (parada != 1):
    n = float(input('Informe o primeiro valor: '))
    m = float(input('Informe o segundo valor: '))
    operacao = escolhaFunc()

    if operacao == 1:
        Soma(n, m)
    elif operacao == 2:
        Subtracao(n, m)
    elif operacao == 3:
        Multiplicacao(n, m)
    elif operacao == 4:
        Divisao(n, m)
    elif operacao == 5:
        break
    else:
        print('Opção inválida! Tente novamente.')
        continue
# ---------------------------------------------------