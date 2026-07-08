# Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente 
# tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter 
# exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro 
# caractere que não seja um número, o programa deve exibir uma mensagem de erro.

# Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 
# 11 dígitos e contém apenas números.

# Exemplo de entrada:
# Digite seu CPF: 12345678901

# Saída esperada:
# CPF válido.

# Se for inválido:
# Digite seu CPF: 1234abc567  
# Erro: O CPF deve conter apenas números.  

# Se o CPF tiver um número de dígitos diferente de 11:
# Digite seu CPF: 1234567  
# Erro: O CPF deve ter exatamente 11 dígitos.  

def validar_cpf(cpf): # Verificar se o CPF é válido
    if not cpf.isdigit(): # Confere se o CPF tem apenas números
        print('Erro: O CPF deve conter apenas números!\n')
        return False
    
    if len(cpf) != 11: # Confere se o CPF contém 11 dígitos
        print('Erro: O CPF deve conter 11 dígitos!\n')
        return False
    
    print('CPF válido.') 
    return True # Se CPF válido, retorna True

def ler_cpf(mensagem): # Lê o CPF e chama a função de validar CPF
    while True:
        numero_cpf = input(mensagem) # R
        if validar_cpf(numero_cpf):
            return numero_cpf

# main() para executar o programa
def main():
    ler_cpf('Digite seu CPF (apenas números): ')

if __name__ == '__main__':
    main()
