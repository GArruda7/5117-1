"""
Lista de uma dimensão, vendas de combustivel grupo central
"""

#1 cria lista com nomes das ilhas

#Pede valores para cada ilha

#apresenta: total - valor minimo e ilhas com esse valor - valor máximo e ilhas com esse valor - ordena de forma crescente e decrescente

ilhas = ['pico', 'terceira', 'graciosa', 'faial', 'saojorge']
ilhasmenor = []
ilhasmaior = []
vendas = [0, 0, 0, 0, 0]
total = 0
minimo = 0
maximo = 0
casa = 0

for ilha in ilhas:
    print(f'Insira as vendas para {ilha}')
    vendas[casa] = int(input())
    total += vendas[casa]
    if casa == 0:
        minimo = vendas[casa]
        maximo = vendas[casa]
    else:
        if vendas[casa] < minimo:
            minimo = vendas[casa]
        if vendas[casa] > maximo:
            maximo = vendas[casa]
    casa += 1

print(f"vendas = {vendas} total = {total} minimo = {minimo} maximo = {maximo}")

ilhasmenor = [ilha for ilha, venda in zip(ilhas, vendas) if venda == minimo]
print(f"As ilhas que venderam menos foram: {','.join(ilhasmenor)} com {minimo}")

ilhasmaior = [ilha for ilha, venda in zip(ilhas, vendas) if venda == maximo]
print(f"As ilhas que venderam mais foram: {','.join(ilhasmenor)} com {maximo}")