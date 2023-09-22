"""
Exercício com lista
"""

#1. Crie uma lista vazia
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]

maior = lista[0]
casamaior = 0
casa = 0

for num in lista:
    if num > maior:
        maior = num
        casamaior = casa
        casa = casa + 1
        print(casa)
    casa= (casa)
print(f"O maior número é {maior} e está na casa {casamaior}")
