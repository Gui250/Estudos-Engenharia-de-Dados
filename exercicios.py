from typing import Dict, Any 

livros: Dict[str, Any] = { 
  
}

# lista_elementos: list = livros.items()

lista_de_livros_usando_dict: dict = { 
  "livro_01": {
    "titulo": "Hábitos Atômicos",
    "Autor": "James Clear",
    "Ano": 2005
  },
  "livro_02": {
      "titulo": "Game Of Thrones",
      "Autor": "Teste",
      "Ano": 2010
  }
}

print(lista_de_livros_usando_dict["livro_01"])