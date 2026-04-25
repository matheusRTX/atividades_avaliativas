from calculo import periodo, meta # Esta linha importa apenas as funções que eu quero usar do arquivo calculo.py
import dados # Esta linha importa o arquivo dadoscsv.py inteiro, para usar as funções de salvar em .csv

def menu():
    while True:
        print("\n=== SIMULADOR DE INVESTIMENTOS TABAJARA ===")
        print("1. Simular por Tempo Fixo")
        print("2. Calcular Tempo para Meta")
        print("0. Sair")
       
        opcao = input("Escolha uma opção: ")
       
        if opcao == '1':
            simulacao_lista, simulacao_dicionario = periodo()
            dados.menu_salvar(simulacao_lista, simulacao_dicionario)
            """
            Criei uma função menu_salvar dentro do arquivo dados.py, para evitar a repetição de código,
            já que as duas simulações (período e meta) retornam os mesmos tipos de dados (lista de listas e lista de dicionários).
            Assim, a função menu_salvar recebe as duas listas como parâmetros e executa as funções de salvar em .csv e .json, evitando a repetição de código.
            """          
        elif opcao == '2':
            simulacao_lista, simulacao_dicionario = meta()
            dados.menu_salvar(simulacao_lista, simulacao_dicionario)     
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__": # Indica onde o programa começa
    menu()
