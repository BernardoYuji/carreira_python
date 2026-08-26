valores = input("Digite os valores das vendas: ").split()
total = sum(map(float, valores))
print(f"O valor total de vendas foi: {total}")