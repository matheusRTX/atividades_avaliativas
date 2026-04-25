import csv
import json
from datetime import datetime

def hora_atual():
    agora = datetime.now()
    return agora.strftime("%Y%m%d%H%M")
    """
    Esta função foi criada para retornar uma string com a hora atual formatada da seguinte maneira:
    202604250720, para que possa ser inserida no nome do arquivo, evitando que arquivos sejam sobrescritos e facilitando a organização dos arquivos salvos.
    """

# Se é lista de dicionários, execute
def salvar_csv_de_dicionarios(arquivo, lista_dados):
    CAMPOS = ["mes", "rendimento", "saldo"]
    with open(f"{arquivo}_{hora_atual()}_dicio.csv", "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader() 
        escritor.writerows(lista_dados)

# Se é lista de listas ou tuplas, execute
def salvar_csv_de_listas(arquivo, lista_dados):
    CAMPOS = ["mes", "rendimento", "saldo"]
    with open(f"{arquivo}_{hora_atual()}_lista.csv", "w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(CAMPOS)
        escritor.writerows(lista_dados)

def salvar_json_de_dicionarios(arquivo, lista_dados, tipo):
    with open(f"{arquivo}_{hora_atual()}_{tipo}.json", "w", encoding="utf-8") as f:
        json.dump(lista_dados, f, ensure_ascii=False, indent=4)
        """
        Observe que a função serve tanto para salvar a lista de dicionários, quanto para salvar a lista de listas,
        Inseri no nome do arquivo o tipo de dado de origem para que possa ser corretamente avaliado e compreendido.
        """


def menu_salvar(simulacao_lista, simulacao_dicionario):
    if len(simulacao_lista) > 0: # Verifica se a simulação retornou uma lista com dados, ou seja, se o usuário digitou valores válidos.
        nome = input("Digite o nome do arquivo para salvar: ")
        salvar_csv_de_listas(nome, simulacao_lista)
        salvar_csv_de_dicionarios(nome, simulacao_dicionario)
        salvar_json_de_dicionarios(nome, simulacao_lista, "lista")
        salvar_json_de_dicionarios(nome, simulacao_dicionario, "dicionario")
        

