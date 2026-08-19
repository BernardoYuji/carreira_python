valor_conta = float(input("Digite o valor da conta: "))
porcentagem = int(input("Digite o valor da porcentagem: "))
calculo_porcentagem = (porcentagem/100)*valor_conta
valor_total = (calculo_porcentagem + valor_conta)
print(f"Valor total a pagar: {valor_total}")