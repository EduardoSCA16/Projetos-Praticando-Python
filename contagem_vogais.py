def contar_vogais(texto): # Função para contar as vogais de um texto
    vogais = 'aeiou'
    contagem = 0

    for letra in texto.lower(): # Percorrer o texto e contar as vogais
        if letra in vogais:
            contagem += 1
            
    return contagem

texto = input('Digite um texto: ')
print(f'Total vogais: {contar_vogais(texto)}')