lista = [10, 20, 20, 15, 5, 60, 140, 80, 20, 20, 15, 5, 60, 140, 1, 15, 21, 34, 45, 56, 67, 8, 3, 23, 11]

# Imprime no número de casas da lista
print(len(lista))

#Imprime a sequência de números entre zero e o número de casas da lista menos um. Usa a variável x
for x in range(len(lista)):
    print(x)

#Imprime a sequencia de numeros entre número de casas da lista menks um e zero. Usa a variável y
numero = len(lista) - 1
for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar')
