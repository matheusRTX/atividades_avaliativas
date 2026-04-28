# Importa as funções `periodo` e `meta` do módulo `calculo`.
from calculo import periodo, meta
# Importa o módulo `dados` inteiro, que contém as funções para salvar dados.
import dados

# Define a função `menu` que exibe o menu principal do simulador.
def menu():
    # Loop infinito para manter o menu ativo até que o usuário escolha sair.
    while True:
        # Imprime o cabeçalho do menu.
        print("\n=== SIMULADOR DE INVESTIMENTOS TABAJARA ===")
        # Imprime as opções do menu.
        print("1. Simular por Tempo Fixo")
        print("2. Calcular Tempo para Meta")
        print("0. Sair")

        # Solicita ao usuário que escolha uma opção.
        opcao = input("Escolha uma opção: ")

        # Verifica a opção escolhida pelo usuário.
        if opcao == '1':
            # Se a opção for '1', chama a função `periodo` para simular por tempo fixo.
            # As funções `periodo` e `meta` retornam duas listas: uma de listas e outra de dicionários.
            simulacao_lista, simulacao_dicionario = periodo()
            # Chama a função `menu_salvar` do módulo `dados` para salvar os resultados.
            dados.menu_salvar(simulacao_lista, simulacao_dicionario)
            """
            Criei uma função menu_salvar dentro do arquivo dados.py, para evitar a repetição de código,
            já que as duas simulações (período e meta) retornam os mesmos tipos de dados (lista de listas e lista de dicionários).
            Assim, a função menu_salvar recebe as duas listas como parâmetros e executa as funções de salvar em .csv e .json, evitando a repetição de código.
            """          
        elif opcao == '2':
            # Se a opção for '2', chama a função `meta` para calcular o tempo até atingir uma meta.
            simulacao_lista, simulacao_dicionario = meta()
            # Chama a função `menu_salvar` do módulo `dados` para salvar os resultados.
            dados.menu_salvar(simulacao_lista, simulacao_dicionario)
        elif opcao == '0':
            # Se a opção for '0', sai do loop e encerra o programa.
            break
        else:
            # Se a opção for inválida, imprime uma mensagem de erro.
            print("Opção inválida.")

# Verifica se o script está sendo executado diretamente (não importado como módulo).
if __name__ == "__main__":
    # Se for o script principal, chama a função `menu` para iniciar o programa.
    menu()
