import json

def salvar_no_arquivo(arquivo, lista_dados):
    with open(arquivo + ".json", "w", encoding="utf-8") as f:
        json.dump(lista_dados, f, ensure_ascii=False, indent=4)
