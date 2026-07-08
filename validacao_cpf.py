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
