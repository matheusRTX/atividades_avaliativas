def periodo():
    try:
        valor_inicial = float(input("Digite o valor inicial: "))
        aporte_mensal = float(input("Digite o aporte mensal: "))
        taxa = float(input("Digite o valor da taxa (em percentual): "))
        meses = int(input("Digite a quantidade de meses: "))
    except:
        print("Valores inválidos, retornando ao menu inicial.")
        return []

    simulacao = []
    rendimento = 0
    for mes in range(1,meses + 1):
        if mes == 1:
            saldo = valor_inicial * (1 + (taxa / 100))
        else:
            valor_inicial = saldo + aporte_mensal
            saldo = valor_inicial * (1 + (taxa / 100))
        rendimento = saldo - valor_inicial
        print(f"Mês: {mes} - Rendimento: R${rendimento:.2f} - Saldo: R${saldo:.2f}")
        dicio = {
            "mes": mes,
            "rendimento": round(rendimento,2),
            "saldo": round(saldo,2)
        }
        lista = [mes, round(rendimento,2), round(saldo,2)]
        simulacao.append(lista)
    return simulacao

def meta():
    valor_inicial = float(input("Digite o valor inicial: "))
    aporte_mensal = float(input("Digite o aporte mensal: "))
    taxa = float(input("Digite o valor da taxa (em percentual): "))
    meta = float(input("Digite a meta a ser alcançada: "))
    saldo = valor_inicial
    mes = 1
    while saldo < meta:
        if mes == 1:
            saldo = valor_inicial * (1 + (taxa / 100))
        else:
            valor_inicial = saldo + aporte_mensal
            saldo = valor_inicial * (1 + (taxa / 100))
        rendimento = saldo - valor_inicial
        print(f"Mês: {mes} - Rendimento: R${rendimento:.2f} - Saldo: R${saldo:.2f}")
        dicio = {
            "mes": mes,
            "rendimento": round(rendimento,2),
            "saldo": round(saldo,2)
        }
        simulacao.append(dicio)
        mes += 1
    return simulacao