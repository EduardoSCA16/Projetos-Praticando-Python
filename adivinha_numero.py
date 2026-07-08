import os
import random

def adivinhar_numero():
    numeros = list(range(1, 101))
    numero_aleatorio = random.choice(numeros)

    while True:
        numero = int(input('Tente adivinhar o número (1-100): '))

        try:
            if numero < 1 or numero > 100:
                print('Número fora do intervalo!\n')
                continue
        
            if numero < numero_aleatorio:
                print('Muito baixo! Tente novamente.\n')
                continue
            elif numero > numero_aleatorio:
                print('Muito alto! Tente novamente.\n')
                continue
            else:
                print(f'Parabéns! Você acertou o número {numero_aleatorio}.')
                break

        except ValueError:
            print('Digite um valor válido.\n')
            continue
        
os.system('cls')
adivinhar_numero()