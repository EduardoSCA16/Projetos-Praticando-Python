# Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras 
# para os usuários. Ele quer um programa que crie senhas aleatórias com letras 
# maiúsculas, minúsculas, números e caracteres especiais.

# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo 
# menos uma letra maiúscula, uma minúscula, um número e um caractere especial. 
# Exiba a senha gerada.

# Saída esperada:
# Senha gerada: A1b@C3d$E5f&  

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