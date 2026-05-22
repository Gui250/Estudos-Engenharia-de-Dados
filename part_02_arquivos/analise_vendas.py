import csv 
lista_de_produtos: list = []



def ler_csv(nome_csv):

    with open(f'./{nome_csv}', 'r', encoding='utf-8') as f: 
        arquivo = csv.DictReader(f)
        for row in arquivo: 
            lista_de_produtos.append(row)

        return lista_de_produtos
    

def processar_dados(lista_dicionario):
    lista_dicionario = ler_csv('./vendas.csv')
    resultado = []
    
    for item in lista_dicionario:
        novo_item = {}
        for chave, valor in item.items():
            novo_item[chave] = valor  # aqui você processa cada valor
        resultado.append(novo_item)   # ← FORA do loop interno, DENTRO do externo
    
    return resultado
        

dicionario_processado_produtos = processar_dados(lista_de_produtos)

def calcular_vendas_por_categoria(dicionario_processado): 
    venda_por_categoria = {}

    for item in dicionario_processado: 
        categoria = item['Categoria']
        preco = float(item['Venda'])
        quantidade = int(item['Quantidade'])

        venda_por_categoria[categoria] = preco * quantidade

    return dict(venda_por_categoria)


print(calcular_vendas_por_categoria(dicionario_processado_produtos))