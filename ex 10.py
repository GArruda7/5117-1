#cria uma lista com os nomes das ilhas do grupo central

ilhas = ['pico, terceira, graciosa, faial, saojorge']

print(len(ilhas))

#cria uma lista com 5 casas, inicializadas a zero

vendas = [0, 0, 0, 0, 0]

#pede ao utilizador para inserir vendas para cada ilha

total = 0
casa = 0

for ilha in ilhas:
    print(f'Insira as vendas para{ilha}')
    vendas[casa] = int(input())
    casa = casa + 1

for venda in vendas:
    total = total + venda

print(vendas)
print(total)
















#pico= input("Insira as vendas para o pico")
#terceira= input("insira as vendas para a terceira")
#graciosa= input("insira as vendas para a graciosa")
#faial= input("insira as vendas para o faial")
#saojorge= input("insira as vendas para saojorge")

#for x in vendas:
    #if x == 'pico':
        #input("Insira as vendas para o pico: ")
    #elif x == 'terceira':
        #input("Insira as vendas para a terceira: ")
    #elif x == 'graciosa':
        #input("Insira as vendas para a graciosa: ")
    #elif x == 'faial':
        #input("Insira as vendas para o faial: ")
    #elif x == 'saojorge':
        #input("Insira as vendas para saojorge: ")

