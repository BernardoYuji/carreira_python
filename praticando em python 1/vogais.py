def contar_vogais(texto):
    vogais = "aeiou"
    quantidade = 0

    for letra in texto.lower():
        if letra in vogais:
            quantidade += 1
        
        return quantidade

texto = int("Digite um texto: ")

print(f"O texto contém {contar_vogais(texto)} vogais.")