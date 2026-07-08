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