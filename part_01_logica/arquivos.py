import csv 

caminho_do_arquivo: str = "./exemplo.csv"

arquivo_csv: csv = []

with open(file=caminho_do_arquivo, mode="r" ,encoding='utf-8') as file:
    leitor_de_csv = csv.DictReader(file)

    for linha in leitor_de_csv: 
        arquivo_csv.append(linha)

print(arquivo_csv)
