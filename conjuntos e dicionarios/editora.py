texto_1 =  set(input("Digite o texto 1"))
texto_2 = set(input("Digite o texto 2"))

palavras_em_comum = texto_1.intersection(texto_2)

print(f"Palavras em comum: {palavras_em_comum}")