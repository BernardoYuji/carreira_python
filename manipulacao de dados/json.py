import json

dados = {
    'nome': 'Bernardo',
    'idade': 19,
    'endereco': ['a', 'b']
}

with open('dados.json', 'w') as f:
    json.dumps(dados, f)

with open('dados.json', 'r') as f:
    dados_lidos = json.load(f)
    print(dados_lidos)