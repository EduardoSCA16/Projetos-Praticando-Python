# Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. 
# Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, 
# e o jogador tem que adivinhar qual é.

# Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, 
# impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

# Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita 
# que o usuário tente adivinhar o número. O programa deve informar se o palpite é 
# maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar 
# um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada.

# Exemplo de entrada:
# Tente adivinhar o número (1-100): 50  

# Saída esperada:
# Parabéns! Você acertou o número 37.  

# Caso o número esteja abaixo:
# Muito baixo! Tente novamente: 17   

# Agora, caso esteja acima:
# Muito alto! Tente novamente: 75    

# Em caso de exceção:
# Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.
# Entrada inválida: invalid literal for int() with base 10: 'abc12

import os
import random

def adivinhar_numero():
    numero_aleatorio = random.randint(1, 100)

    while True:
        try:
            numero = int(input('Tente adivinhar o número (1-100): '))

            if numero < 1 or numero > 100:
                raise ValueError('Número fora do intervalo!\n')
        
            if numero < numero_aleatorio:
                print('Muito baixo! Tente novamente.\n')
            elif numero > numero_aleatorio:
                print('Muito alto! Tente novamente.\n')
            else:
                print(f'Parabéns! Você acertou o número {numero_aleatorio}.')
                break

        except ValueError as e:
            print(f'Digite um valor válido. Erro: {e}\n')
            continue
        
os.system('cls')
adivinhar_numero()