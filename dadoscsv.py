import csv

# Se é lista de dicionários, execute
def salvar_no_arquivo(arquivo, lista_dados):
    CAMPOS = ["mes", "rendimento", "saldo"]
    with open(arquivo + ".csv", "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader() 
        escritor.writerows(lista_dados)

# Se é lista de listas ou tuplas, execute
def salvar_lista(arquivo, lista_dados):
    CAMPOS = ["mes", "rendimento", "saldo"]
    with open(arquivo + ".csv", "w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(CAMPOS)
        escritor.writerows(lista_dados)
