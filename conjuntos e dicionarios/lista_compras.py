lista_laura = set(input("Lista de Laura: ").split(","))
lista_ana = set(input("Lista de Ana: ").split(","))

ambas_listas = lista_laura.intersection(lista_ana)
exclusivos_laura = lista_laura.difference(lista_ana)
exclusivos_ana = lista_ana.difference(lista_laura)

print(f"Itens em ambas as listas: {',' .join (ambas_listas)}")
print(f"Itens exclusivos de Laura: {',' .join(exclusivos_laura)}")
print(f"Itens exclusivos de Ana: {',' .join(exclusivos_ana)}")