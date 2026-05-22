import pandas as pd 

class ProcessadorCSV:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.arquivo_csv)

    def remover_vazios(self): 
        self.df = self.df.dropna()

    def carregar_e_filtrar(self, filtro):
        df = pd.read_csv(self.arquivo_csv)

        df = df.dropna()

        df_filtrado = df[df['Categoria'] == filtro]

        return df_filtrado
    
    def processar(self, filtro): 
        self.carregar_csv()
        self.remover_vazios()
        self.carregar_e_filtrar(filtro)

        return self.df
    

arquivo = 'vendas.csv'
filtro = 'Electronics'
processador = ProcessadorCSV(arquivo)

df_filtrado = processador.processar(filtro)

print(df_filtrado)
