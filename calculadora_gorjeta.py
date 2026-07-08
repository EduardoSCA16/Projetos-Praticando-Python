# João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes 
# deixam ao pagar a conta. O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem 
# escolher dar mais ou menos. Para agilizar o processo, João quer um programa que receba o 
# valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. 
# O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

# Exemplo de entrada:
# Digite o valor da conta: 120.00  
# Digite a porcentagem de gorjeta: 10  

# Saída esperada:
# Valor da gorjeta: R$ 12.00  
# Total a pagar: R$ 132.00

# Função que recebe uma mensagem e verifica se o valor dela é do tipo float
def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem)) # Recebe o valor que deve ser float
            if valor < 0: # Se valor for menor que zero 
                print('Os valores não podem ser negativos.\n')
                continue
            return valor
        except ValueError: # Caso valor seja diferente de float
            print('Digite um valor válido.\n')

# Função de calcular a gorjeta
def calcular_gorjeta(total, porcentagem):
    return total * (porcentagem / 100)

# main para rodar o projeto
def main():
    # Chama a função ler_float()
    valor_total = ler_float('Digite o valor total da conta (R$): ')
    porcentagem_gorjeta = ler_float('Digite a porcentagem de gorjeta (%): ')

    # Calcula a gorjeta e o total a pagar
    valor_gorjeta = calcular_gorjeta(valor_total, porcentagem_gorjeta)
    total_a_pagar = valor_total + valor_gorjeta

    # Mensagem final do projeto
    print(f'\nValor da gorjeta: R$ {valor_gorjeta:.2f}')
    print(f'Valor total a pagar: R$ {total_a_pagar:.2f}')

if __name__ == '__main__':
    main()