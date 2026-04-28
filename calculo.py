# Define a função `periodo` que simula investimentos por um período fixo.
def periodo():
    try:
        # Solicita ao usuário o valor inicial do investimento e converte para float.
        valor_inicial = float(input("Digite o valor inicial: "))
        # Solicita ao usuário o valor do aporte mensal e converte para float.
        aporte_mensal = float(input("Digite o aporte mensal: "))
        # Solicita ao usuário a taxa de rendimento (em percentual) e converte para float.
        taxa = float(input("Digite o valor da taxa (em percentual): "))
        # Solicita ao usuário a quantidade de meses e converte para inteiro.
        meses = int(input("Digite a quantidade de meses: "))
    except:
        # Em caso de erro na entrada de dados, imprime uma mensagem e retorna uma lista vazia.
        print("Valores inválidos, retornando ao menu inicial.")
        # NOTA: Retornamos ambas as listas vazias para manter a sincronia e consistência.
        return [], [] 
    # Inicializa uma lista para armazenar os dados da simulação como listas (para CSV).
    simulacao_lista = []
    # Inicializa uma lista para armazenar os dados da simulação como dicionários (para CSV e JSON).
    simulacao_dicionario = []
    # Inicializa a variável de rendimento.
    rendimento = 0
    # Loop que itera por cada mês do período de simulação.
    for mes in range(1, meses + 1):
        """
        O Loop for nesta situação é mais indicado, pois conhecemos exatamente a quantidade de vezes (meses)
        que o código deverá rodar.
        """
        # Se for o primeiro mês, o saldo é calculado com base apenas no valor inicial.
        if mes == 1:
            saldo = valor_inicial * (1 + (taxa / 100))
        else:
            # Nos meses seguintes, o valor inicial é atualizado com o saldo anterior mais o aporte mensal.
            valor_inicial = saldo + aporte_mensal
            # O novo saldo é calculado com base no valor inicial atualizado e na taxa.
            saldo = valor_inicial * (1 + (taxa / 100))
        # O rendimento do mês é a diferença entre o saldo atual e o valor inicial do mês.
        rendimento = saldo - valor_inicial
        # Imprime os resultados do mês formatados.
        print(f"Mês: {mes} - Rendimento: R${rendimento:.2f} - Saldo: R${saldo:.2f}")
        # Cria um dicionário com os dados do mês.
        dicio = {
            "mes": mes,
            "rendimento": round(rendimento, 2),
            "saldo": round(saldo, 2)
        }
        # Cria uma lista com os dados do mês.
        lista = [mes, round(rendimento, 2), round(saldo, 2)]
        # Adiciona a lista à `simulacao_lista`.
        simulacao_lista.append(lista)
        # Adiciona o dicionário à `simulacao_dicionario`.
        simulacao_dicionario.append(dicio)
    # Retorna as duas listas contendo os dados da simulação.
    return simulacao_lista, simulacao_dicionario

# Define a função `meta` que simula investimentos até atingir uma meta específica.
def meta():
    try:
        # Solicita ao usuário o valor inicial do investimento e converte para float.
        valor_inicial = float(input("Digite o valor inicial: "))
        # Solicita ao usuário o valor do aporte mensal e converte para float.
        aporte_mensal = float(input("Digite o aporte mensal: "))
        # Solicita ao usuário a taxa de rendimento (em percentual) e converte para float.
        taxa = float(input("Digite o valor da taxa (em percentual): "))
        # Solicita ao usuário o valor da meta a ser alcançada e converte para float.
        meta = float(input("Digite a meta a ser alcançada: "))
    except:
        # Em caso de erro na entrada de dados, imprime uma mensagem e retorna uma lista vazia.
        print("Valores inválidos, retornando ao menu inicial.")
        # NOTA: Retornamos ambas as listas vazias para manter a sincronia e consistência.
        return [], [] 
    # Inicializa uma lista para armazenar os dados da simulação como listas.
    simulacao_lista = []
    # Inicializa uma lista para armazenar os dados da simulação como dicionários.
    simulacao_dicionario = []
    # Inicializa o saldo com o valor inicial.
    saldo = valor_inicial
    # Inicializa o contador de meses.
    mes = 1
    # Loop `while` que continua enquanto o saldo for menor que a meta.
    while saldo < meta:
        """
        O cálculo de meta pode ser feito da mesma maneira que o cálculo de período,
        porém, como não sei exatamente quantos meses serão necessários para alcançar a meta,
        o Loop While é mais indicado, pois ele vai rodar até que a condição (saldo < meta) seja falsa.
        Mudei também a lógica do cálculo, para exemplificar outra maneira de se calcular o rendimento.
        """
        # Se não for o primeiro mês, adiciona o aporte mensal ao valor inicial.
        if mes != 1:
            valor_inicial = saldo + aporte_mensal
        # Calcula o rendimento do mês com base no valor inicial e na taxa.
        rendimento = valor_inicial * (taxa / 100)
        # Atualiza o saldo somando o valor inicial e o rendimento.
        saldo = valor_inicial + rendimento
        # Imprime os resultados do mês formatados.
        print(f"Mês: {mes} - Rendimento: R${rendimento:.2f} - Saldo: R${saldo:.2f}")
        # Cria um dicionário com os dados do mês.
        dicio = {
            "mes": mes,
            "rendimento": round(rendimento, 2),
            "saldo": round(saldo, 2)
        }
        # Cria uma lista com os dados do mês.
        lista = [mes, round(rendimento, 2), round(saldo, 2)]
        # Adiciona a lista à `simulacao_lista`.
        simulacao_lista.append(lista)
        # Adiciona o dicionário à `simulacao_dicionario`.
        simulacao_dicionario.append(dicio)
        # Incrementa o contador de meses.
        mes += 1
    # Retorna as duas listas contendo os dados da simulação.
    return simulacao_lista, simulacao_dicionario
