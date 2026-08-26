def contador_caracteres(palavra):
    return len(palavra)

texto = input("Digite uma palavra: ")
print(f"Essa palavra tem {contador_caracteres(texto)} caracteres")