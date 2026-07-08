# Ana precisa de um programa simples para gerenciar suas tarefas diárias. 
# Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

# Crie um programa com um menu interativo que permita ao usuário adicionar, 
# visualizar e remover tarefas. Use uma lista para armazenar as tarefas.

# Exemplo de entrada:
# 1. Adicionar tarefa 
# 2. Visualizar tarefas 
# 3. Remover tarefa 
# 4. Sair
# Escolha uma opção: 1

# Saída esperada:
# Digite a tarefa: Estudar Python
# Tarefa adicionada!

# Caso selecione a opção 2 ao adicionar uma tarefa:
# Tarefas:
# 1. Estudar Python

# Caso selecione a opção 3 com uma tarefa adicionada:
# Digite o número da tarefa a ser removida: 1
# Tarefa 'Estudar Python' removida!

# Caso selecione a opção 3 sem uma tarefa adicionada:
# Digite o número da tarefa a ser removida: Estudar Python
# Erro: Nenhuma tarefa para remover.

# Caso selecione a opção 3 com uma opção inválida:
# Escolha uma opção: 3
# Digite o número da tarefa a ser removida: ABC
# Erro: Entrada inválida! Digite um número.

# Caso selecione nenhuma das opções listadas:
# Escolha uma opção: 5
# Erro: Opção inválida! Escolha uma opção entre 1 e 4.

# Caso selecione a opção 4:
# Escolha uma opção: 4 
# Saindo do gerenciador de tarefas. Até mais!

import os
import sys

tarefas = []

def adicionar_tarefa():
    limpar_tela()
    mostrar_subtitulo('Adicionar Tarefa')
    
    tarefa = input('Digite a tarefa: ').strip()
    if tarefa:
        tarefas.append(tarefa)
        print('Tarefa adicionada!')
    else:
        print('Erro: A tarefa não pode estar vazia.')

    voltar_menu()

def visualizar_tarefas():
    limpar_tela()
    mostrar_subtitulo('Visualizar Tarefas')
    contador = 1

    if tarefas:
        for i in tarefas:
            print(f'{contador}- {i}')
            contador += 1
    else:
        print('Nenhuma tarefa encontrada.')

    voltar_menu()

def remover_tarefa():
    limpar_tela()
    if not tarefas:
        print('Erro: Nenhuma tarefa para remover.')
        voltar_menu()
        return

    try:
        indice = int(input('Digite o número da tarefa a ser removida: ')) - 1

        if 0 <= (indice) < len(tarefas):
            removida = tarefas.pop(indice)
            print(f"Tarefa '{removida}' removida!")
        else:
            print('Erro: Índice inválido! Digite um número.')
    except ValueError:
        print('Erro: Entrada inválida! Digite um número.')
    
    voltar_menu()

def sair():
    print('\nFinalizando Gerenciador de Tarefas. Até mais!\n')
    sys.exit()

def mostrar_subtitulo(texto):
    linhas = ('-' * len(texto))

    print(linhas)
    print(texto)
    print(linhas)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_menu():
    input('\nDigite qualquer tecla para voltar: ')
    main()

def mostrar_menu():
    print('Bem-vindo ao Gerenciador de Tarefas!\n')
    print('1. Adicionar tarefa') 
    print('2. Visualizar tarefas' ) 
    print('3. Remover tarefa' ) 
    print('4. Sair')

def escolher_opcao():
    while True:
        try:
            opcao = int(input('\nEscolha uma opção: '))
            if opcao == 1:
                return adicionar_tarefa()
            elif opcao == 2:
                return visualizar_tarefas()
            elif opcao == 3:
                return remover_tarefa()
            elif opcao == 4:
                return sair()
            else:
                print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
        except ValueError:
            print('Erro: Entrada inválida. Tente novamente.')
            continue

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    mostrar_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()