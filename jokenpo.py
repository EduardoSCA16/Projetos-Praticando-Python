# Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. 
# Ele precisa de um programa que permita ao usuário escolher uma opção e depois 
# exiba o resultado da partida.

# Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. 
# O computador escolherá aleatoriamente uma opção. O programa deve exibir quem 
# venceu a partida. Lembrando que:

# Pedra ganha de Tesoura (Pedra quebra Tesoura);
# Tesoura ganha de Papel (Tesoura corta Papel);
# Papel ganha de Pedra (Papel cobre Pedra);
# Se ambos escolherem a mesma opção, é um empate.

# Exemplo de entrada:
# Escolha: pedra, papel ou tesoura? papel  

# Saída esperada:
# Computador escolheu: pedra
# Você venceu!  

# Caso o computador vença:
# Computador escolheu: tesoura  
# Você perdeu!  

# Caso o computador escolha a mesma opção que você:
# Computador escolheu: papel 
# Empate!

import random

def jogar_jokenpo():
    while True:
        jokenpo = ['pedra', 'papel', 'tesoura']
        escolha = input('Escolha: pedra, papel ou tesoura? ').lower()

        if escolha not in jokenpo:
            print('Opção errada!\n')
            continue
        
        escolha_computador = random.choice(jokenpo)

        if escolha_computador == 'pedra' and escolha == 'papel':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Você venceu!\n'
            )
        elif escolha_computador == 'pedra' and escolha == 'tesoura':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Você perdeu!\n'
            )
        elif escolha_computador == 'pedra' and escolha == 'pedra':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Empate!\n'
            )
        elif escolha_computador == 'papel' and escolha == 'pedra':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Você perdeu!\n'
            )
        elif escolha_computador == 'papel' and escolha == 'papel':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Empate!\n'
            )
        elif escolha_computador == 'papel' and escolha == 'tesoura':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Você venceu!\n'
            )
        elif escolha_computador == 'tesoura' and escolha == 'pedra':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Você venceu!\n'
            )
        elif escolha_computador == 'tesoura' and escolha == 'papel':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Você perdeu!\n'
            )
        elif escolha_computador == 'tesoura' and escolha == 'tesoura':
            return (
                f'Computador: {escolha_computador}\n'
                f'Você: {escolha}\n'
                f'Empate!\n'
            )

def main():
    print(jogar_jokenpo())

if __name__ == '__main__':
    main()