import json
from typing import Dict, Any

dicionario: Dict[str, Any] = { 
    "nome": "Sapato",
    "quantidade": 39,
    "preco": 10.58,
    "disponibilidade": True
}


produto_02: dict = {
    "nome": "Televisão",
    "quantidade": 10,
    "preco": 70.38,
    "disponibilidade": True
}

carrinho: list = []

carrinho.append(dicionario)
carrinho.append(produto_02)

print(carrinho)

# transformando carrinho em json
carrinho_json = json.dumps(carrinho)

print(carrinho_json)