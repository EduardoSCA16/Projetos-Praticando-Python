def contador_palavras_longas(texto): # Esta função cria uma lista com palavras longas
    palavras_longas = []
    for palavra in texto.split():
        if len(palavra) > 10: # Palavras com mais de 10 caracteres
            palavras_longas.append(palavra)

    return palavras_longas

texto = input('Digite o texto: ')
palavras_longas = contador_palavras_longas(texto)

if not palavras_longas:
    print('Nenhuma palavra longa encontrada.')
else:
    print('Palavras longas encontradas:', ', '.join(palavras_longas))
