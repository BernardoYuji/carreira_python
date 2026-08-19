convidados = set()

while True:
    nome = input("Digite o nome do convidado or 'sair' para encerrar: ")
    
    if nome.lower() == "sair":
        break
    convidados.add(nome)
print(f"Convidados confirmados: {',' .join(convidados)}")