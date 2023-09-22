# Imprime a lista na ordem inversa
lista = [10, 10, 7, 4, 20, 34, 55, 23, 11]

# Imprimir os elementos da lista e dizer se é par ou ímpar

print(lista)
print()


for x in lista:
    if x % 2 == 0:
        print(f"{x} é par")
    else:
        x % 3 == 0
        print(f"{x} é ímpar")
