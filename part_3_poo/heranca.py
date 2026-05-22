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
        self.carregar_dados(dados_extraidos)


class ETLCSV(ETLProcess):
    pass