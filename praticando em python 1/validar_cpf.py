def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: CPF deve conter apenas números"
    if len(cpf) != 11:
        return "Erro: número de dígitos deve ter exatamente 11 dígitos"
    return "CPF válido"

cpf = input("Digite seu CPF: ")
print(validar_cpf(cpf))