import pandas as pd 

class CsvProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None


    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, coluna ,filtro):
        if len(coluna) != len(filtro):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        
        if len(coluna) == 0: 
            return self.df
        
        coluna_atual = coluna[0]
        atributo_atual = filtro[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]
        
        if len(coluna) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(coluna[1:], filtro[1:])
    
    def sub_filtro(self, coluna, filtro): 
        return self.df_filtrado[self.df_filtrado[coluna] == filtro]

arquivo_csv = './exemplo.csv'


arquivo_CSV = CsvProcessor(arquivo_csv)

arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(['estado', 'preço'], ['SP', '10,50']))