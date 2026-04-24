from calculo import periodo, meta
import dadoscsv
#import dadosjson

def menu():
    while True:
        print("\n=== SIMULADOR DE INVESTIMENTOS TABAJARA ===")
        print("1. Simular por Tempo Fixo")
        print("2. Calcular Tempo para Meta")
        print("0. Sair")
       
        opcao = input("Escolha uma opção: ")
       
        if opcao == '1':
            simulacao = periodo()
            if len(simulacao) > 0:
                nome = input("Digite o nome do arquivo para salvar: ")
                dadoscsv.salvar_lista(nome, simulacao)
                #dadosjson.salvar_no_arquivo(nome, simulacao)
                #dadoscsv.salvar_no_arquivo(nome, simulacao)
        elif opcao == '2':
            simulacao = meta()
            nome = input("Digite o nome do arquivo para salvar: ")
            #dadosjson.salvar_no_arquivo(nome, simulacao)
            dadoscsv.salvar_no_arquivo(nome, simulacao)        
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__": # Indica onde o programa começa
    menu()
