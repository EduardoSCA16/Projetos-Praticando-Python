# Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o 
# usuário digitar valores inválidos, ele precisa tratar os erros.

# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. 
# Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

# Exemplo de entrada:
# Digite o primeiro número: 5
# Escolha a operação (+, -, *, /): +
# Digite o segundo número: 7

# Saída esperada:
# Resultado: 12

# Caso selecione nenhuma das operações listadas:
# Opção inválida

# Caso digite um caractere em vez de número:
# Erro: Entrada inválida. Digite apenas números.

# Caso tente fazer uma divisão por 0:
# Erro: Divisão por zero não é permitida.

import os

def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError
    return n1 / n2

def calculadora():
    operacoes = ['+', '-', '*', '/']
    while True:
        try:
            num1 = float(input('Digite o primeiro número: '))
            operacao = input('Escolha a operação (+, -, *, /): ')
            num2 = float(input('Digite o segundo número: '))

            if operacao not in operacoes:
                print('Erro: Opção inválida.\n')
                continue
        
        except ValueError:
            print('Erro: Entrada inválida. Digite apenas números.\n')
            continue

        except ZeroDivisionError:
            print('Erro: Divisão por zero não é permitida.')
            continue

        if operacao == '+':
            print(f'\nA soma entre {num1} e {num2} é: {soma(num1, num2):.2f}')
            break
        elif operacao == '-':
            print(f'\nA subtração entre {num1} e {num2} é: {subtracao(num1, num2):.2f}')
            break
        elif operacao == '*':
            print(f'\nA miltiplicação entre {num1} e {num2} é: {multiplicacao(num1, num2):.2f}')
            break
        elif operacao == '/':
            print(f'\nA divisão entre {num1} e {num2} é: {divisao(num1, num2):.2f}')
            break

os.system('cls')
calculadora()