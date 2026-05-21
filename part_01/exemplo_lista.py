produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []

# Adicionando produtos
produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)
print(produtos)

# Tirando o último elemento
produtos.pop()

print(produtos)

numeros = []

# Coloca numeros de 0 a 4 na lista
numeros.extend(range(0, 5))

print(numeros)