# Matriz de 3 x 3
matriz = [
    [9, 6, 3],
    [5, 1, 2],
    [8, 4, 7]
]
print(matriz)
# funcion buscar_valor especifico
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j
valor_buscado = 1
print(buscar_valor(matriz,valor_buscado))

if valor_buscado == valor_buscado:
    print("valor encontrado en la posición",buscar_valor(matriz,valor_buscado))
else:
    print("valor inexistente")
