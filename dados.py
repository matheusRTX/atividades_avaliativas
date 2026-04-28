# Importa o módulo `csv` para lidar com operações de leitura e escrita de arquivos CSV.
import csv
# Importa o módulo `json` para lidar com operações de serialização e desserialização de dados JSON.
import json
# Importa a classe `datetime` do módulo `datetime` para trabalhar com datas e horas.
from datetime import datetime

# Define a função `hora_atual` que retorna a data e hora atuais formatadas.
def hora_atual():
    # Obtém a data e hora atuais.
    agora = datetime.now()
    # Formata a data e hora para uma string no formato 'YYYYMMDDHHMM' e a retorna.
    return agora.strftime("%Y%m%d%H%M")
    """
    Esta função foi criada para retornar uma string com a hora atual formatada da seguinte maneira:
    202604250720, para que possa ser inserida no nome do arquivo, evitando que arquivos sejam sobrescritos e facilitando a organização dos arquivos salvos.
    """

# Define a função `salvar_csv_de_dicionarios` para salvar uma lista de dicionários em um arquivo CSV.
def salvar_csv_de_dicionarios(arquivo, lista_dados):
    # Define os nomes dos campos (cabeçalhos) para o arquivo CSV.
    CAMPOS = ["mes", "rendimento", "saldo"]
    # Abre o arquivo CSV em modo de escrita ('w'), com codificação UTF-8 e sem linhas em branco entre as linhas.
    # NOTA: A extensão '.csv' é adicionada automaticamente aqui, você não precisa digitá-la.
    with open(f"{arquivo}_{hora_atual()}_dicio.csv", "w", encoding="utf-8", newline="") as f:
        # Cria um objeto `csv.DictWriter` que mapeia dicionários para linhas CSV.
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        # Escreve a linha de cabeçalho no arquivo CSV.
        escritor.writeheader()
        # Escreve todas as linhas de dados (dicionários) no arquivo CSV.
        escritor.writerows(lista_dados)

# Define a função `salvar_csv_de_listas` para salvar uma lista de listas (ou tuplas) em um arquivo CSV.
def salvar_csv_de_listas(arquivo, lista_dados):
    # Define os nomes dos campos (cabeçalhos) para o arquivo CSV.
    CAMPOS = ["mes", "rendimento", "saldo"]
    # Abre o arquivo CSV em modo de escrita ('w'), com codificação UTF-8 e sem linhas em branco entre as linhas.
    # NOTA: A extensão '.csv' é adicionada automaticamente aqui, você não precisa digitá-la.
    with open(f"{arquivo}_{hora_atual()}_lista.csv", "w", encoding="utf-8", newline="") as f:
        # Cria um objeto `csv.writer` para escrever linhas CSV.
        escritor = csv.writer(f)
        # Escreve a linha de cabeçalho no arquivo CSV.
        escritor.writerow(CAMPOS)
        # Escreve todas as linhas de dados (listas) no arquivo CSV.
        escritor.writerows(lista_dados)

# Define a função `salvar_json_de_dicionarios` para salvar dados (dicionários ou listas) em um arquivo JSON.
def salvar_json_de_dicionarios(arquivo, lista_dados, tipo):
    # Abre o arquivo JSON em modo de escrita ('w'), com codificação UTF-8.
    # NOTA: A extensão '.json' é adicionada automaticamente aqui, você não precisa digitá-la.
    with open(f"{arquivo}_{hora_atual()}_{tipo}.json", "w", encoding="utf-8") as f:
        # Serializa a `lista_dados` para o formato JSON e a escreve no arquivo.
        # `ensure_ascii=False` permite caracteres não-ASCII e `indent=4` formata o JSON com indentação de 4 espaços.
        json.dump(lista_dados, f, ensure_ascii=False, indent=4)
        """
        Observe que a função serve tanto para salvar a lista de dicionários, quanto para salvar a lista de listas,
        Inseri no nome do arquivo o tipo de dado de origem para que possa ser corretamente avaliado e compreendido.
        """

# Define a função `menu_salvar` que gerencia o processo de salvar os dados da simulação.
def menu_salvar(simulacao_lista, simulacao_dicionario):
    # Verifica se a `simulacao_lista` contém dados. 
    # NOTA: Como as listas são geradas juntas, se uma tiver dados, a outra também terá.
    if len(simulacao_lista) > 0:
        # Solicita ao usuário um nome base para os arquivos a serem salvos.
        nome = input("Digite o nome do arquivo para salvar: ")
        # Chama a função para salvar a lista de listas em CSV.
        salvar_csv_de_listas(nome, simulacao_lista)
        # Chama a função para salvar a lista de dicionários em CSV.
        salvar_csv_de_dicionarios(nome, simulacao_dicionario)
        # Chama a função para salvar a lista de listas em JSON, indicando o tipo 'lista'.
        salvar_json_de_dicionarios(nome, simulacao_lista, "lista")
        # Chama a função para salvar a lista de dicionários em JSON, indicando o tipo 'dicionario'.
        salvar_json_de_dicionarios(nome, simulacao_dicionario, "dicionario")
    # NOTA: Não há um bloco 'else' aqui porque, se a lista estiver vazia, 
    # o programa simplesmente não faz nada e volta ao menu principal, 
    # já que o erro de entrada já foi tratado e informado nas funções de cálculo.
