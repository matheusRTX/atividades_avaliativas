def periodo():
    try:
        valor_inicial = float(input("Digite o valor inicial: "))
        aporte_mensal = float(input("Digite o aporte mensal: "))
        taxa = float(input("Digite o valor da taxa (em percentual): "))
        meses = int(input("Digite a quantidade de meses: "))
    except:
        print("Valores inválidos, retornando ao menu inicial.")
        return []
    simulacao_lista = [] # Lista que vai receber uma lista com os dados da semana para salvar em um arquivo .csv ou .json
    simulacao_dicionario = [] # Lista que vai receber um dicionário com os dados da semana para salvar em um arquivo .csv ou .json
    rendimento = 0
    for mes in range(1,meses + 1):
        """
        O Loop for nesta situação é mais indicado, pois conhecemos exatamente a quantidade de vezes (meses)
        que o código deverá rodar.
        """
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
        } # Dicionário que contém os dados referentes ao mês atual no loop for
        lista = [mes, round(rendimento,2), round(saldo,2)] # Lista que contém os dados referentes ao mês atual no loop for
        simulacao_lista.append(lista)
        simulacao_dicionario.append(dicio)
    return simulacao_lista, simulacao_dicionario # Esta linha retorna para minha função inicial, duas listas, uma lista de listas e uma lista de dicionários.

def meta():
    try:
        valor_inicial = float(input("Digite o valor inicial: "))
        aporte_mensal = float(input("Digite o aporte mensal: "))
        taxa = float(input("Digite o valor da taxa (em percentual): "))
        meta = float(input("Digite a meta a ser alcançada: "))
    except:
        print("Valores inválidos, retornando ao menu inicial.")
        return []
    simulacao_lista = [] # Lista que vai receber uma lista com os dados da semana para salvar em um arquivo .csv ou .json
    simulacao_dicionario = [] # Lista que vai receber um dicionário com os dados da semana para salvar em um arquivo .csv ou .json
    saldo = valor_inicial
    mes = 1
    while saldo < meta:
        """
        O cálculo de meta pode ser feito da mesma maneira que o cálculo de período,
        porém, como não sei exatamente quantos meses serão necessários para alcançar a meta,
        o Loop While é mais indicado, pois ele vai rodar até que a condição (saldo < meta) seja falsa.
        Mudei também a lógica do cálculo, para exemplificar outra maneira de se calcular o rendimento.
        """
        if mes != 1:
            valor_inicial = saldo + aporte_mensal
        rendimento = valor_inicial * (taxa / 100)
        saldo = valor_inicial + rendimento
        print(f"Mês: {mes} - Rendimento: R${rendimento:.2f} - Saldo: R${saldo:.2f}")
        dicio = {
            "mes": mes,
            "rendimento": round(rendimento,2),
            "saldo": round(saldo,2)
        } # Dicionário que contém os dados referentes ao mês atual no loop for
        lista = [mes, round(rendimento,2), round(saldo,2)] # Lista que contém os dados referentes ao mês atual no loop for
        simulacao_lista.append(lista)
        simulacao_dicionario.append(dicio)
        mes += 1
    return simulacao_lista, simulacao_dicionario # Esta linha retorna para minha função inicial, duas listas, uma lista de listas e uma lista de dicionários.