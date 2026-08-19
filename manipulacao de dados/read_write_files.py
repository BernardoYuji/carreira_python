with open ('dados.txt', 'w') as f:
    f.write('Hello World!')
    
with open('dados.txt', 'r') as f:
    conteudo = f.read()

print(conteudo)