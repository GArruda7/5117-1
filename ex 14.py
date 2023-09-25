"""

"""

vendas = [12, 23, 3, 14, 5, 16, 57, 8, 19]
troquei = True

def ordenar(lista, ordem=1):
    troquei = True
    while troquei:
        troquei = False
        x = 0
        while x < len(vendas) - 1:
            if lista[x] > lista[x + 1]:
               temp = lista[x]
               lista[x] = lista[x + 1]
               lista[x +1 ] = temp
               troquei = True
            x += 1
    return lista

if __name__ == '__main__':
    vendas = [12, 23, 3, 14, 5, 16, 57, 8, 19]
    print(ordenar(vendas))
    print(ordenar(vendas, -1))
