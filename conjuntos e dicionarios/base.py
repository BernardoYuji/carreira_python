conjunto = {1, 2, 3}

adicionar = conjunto.add(4)
atualizar = conjunto.update([5, 6, 7])
remover = conjunto.remove(2) # se nao existir ele gera um KeyError
discard = conjunto.discard(2)
pop = conjunto.pop() # remove e retorna um elemento aleatorio
limpar = conjunto.clear()

# operacao entre conjuntos

a = {1, 2, 3}
b = {3, 4, 5}

unir = a.union(b) # ou a pipe b
intersecao = a.intersection(b) # ou a & b
diferenca = a.difference(b) # ou a - b
simetria = a.symmetric_difference(b) # ou a ^ b