permissoes_principais = set(p.strip() for p in input ("Permissoes principais").lower().split(','))
permissoes_solicitadas = set(p.strip() for p in input ("Permissoes solicitadas").lower().split(','))

eh_subconjunto = permissoes_principais.issubset(permissoes_solicitadas)

if eh_subconjunto:
    print("As permissões solicitadas fazem parte das permissões principais.")
else:
     print("As permissões solicitadas não fazem parte das permissões principais.")