import pandas as pd 

class ETLProcess: 
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados
    
    def extrair_dados(self): 
        raise NotImplementedError("Método extrair dados deve ser implementado nas classes filhas")
    
    def transformar_dados(self, dados):
        raise NotImplementedError("Método transformar dados deve ser implementado nas classes filhas")
    
    def carregar_dados(self, dados_transformados): 
        raise NotImplementedError("Método carregar dados deve ser implementado nas classes filhas")
    
    def etl(self): 
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)


class ETLCSV(ETLProcess):
    def extrair_dados(self): 
        return pd.read_csv(self.fonte_dados)
    
    def transformar_dados(self, dados): 
        return dados.map(lambda x: x.upper() if isinstance(x, str) else x)
    
    def carregar_dados(self, dados_transformados): 
        print("Dados transformados: ")
        print(dados_transformados)


class ETLExcel(ETLProcess):
    def __init__(self, fonte_dados):
        super().__init__(fonte_dados)
    
    def extrair_dados(self):
        return super().extrair_dados()
    
    def transformar_dados(self, dados):
        return "dados transformados"
    
if __name__ == "__main__":
    fonte_csv = 'vendas.csv'
    etl_csv = ETLCSV(fonte_csv)
    etl_csv.etl()