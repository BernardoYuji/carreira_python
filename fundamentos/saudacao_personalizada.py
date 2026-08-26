def saudacao_personalizada(horario):
    if horario < 12:
        return "Bom dia!"
    elif horario >= 12:
        return "Boa tarde!"
    else:
        return "Boa noite!"

hora = int(input("Digite o horário: "))
print(saudacao_personalizada(hora))