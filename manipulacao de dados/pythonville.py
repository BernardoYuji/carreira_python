import csv

alunos = [
    {'nome': 'bernardo', 'nota': 10},
    {'nome': 'beatriz', 'nota': 9}
]

fields = ['nome', 'nota']

with open('alunos.csv', 'w', newline='') as f:
    escritor = csv.DictWriter(f, fieldnames=fields)
    escritor.writeheader()
    escritor.writerows(alunos) 

with open('alunos.csv', 'r', newline='') as f:
    leitor = csv.DictReader(f)
    maior_nota = None
    nome = None
    for linha in leitor:
        nota = int(linha['nota'])
        if maior_nota is None or nota > maior_nota:
            maior_nota = nota
            nome = linha['nome']

    print(f'A maior nota é {maior_nota} e o aluno é {nome}') 
 