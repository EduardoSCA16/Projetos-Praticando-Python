import random
import string

def gerador_de_senha():
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = '!@#$&*'
    aleatorio = maiusculas + minusculas + numeros + caracteres_especiais
    senha = []
    tamanho_senha = 12

    # Selecionando os caracteres exigidos
    senha.append(random.choice(maiusculas))
    senha.append(random.choice(minusculas))
    senha.append(random.choice(numeros))
    senha.append(random.choice(caracteres_especiais))

    # Adicionando o restante dos caracteres até ter 12 caracteres
    for _ in range(tamanho_senha - 4):
        senha.append(random.choice(aleatorio))

    # Embaralhando a senha
    random.shuffle(senha)

    # Transformando a lista em uma string
    senha = ''.join(senha)

    # Imprimindo a senha
    return f'Senha gerada: {senha}'

def main():
    print(gerador_de_senha())

if __name__ == '__main__':
    main()