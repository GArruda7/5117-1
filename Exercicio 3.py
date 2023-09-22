"""
Exercício com lista
"""

lista = [10, 20, 20, 15, 5, 60, 140, 80, 40]
print(lista)


[10, 20, 10, 7.5, 5, 30, 70, 40, 20]

#casa = 0
#for numero in lista:
#    if numero > 20:
#       x = numero / 2
#       lista[casa] = x
#    casa = casa + 1
print(lista)


novalista = []

for numero in lista:
   if numero > 20:
      novalista.append(numero / 2)
   else:
       novalista.append(numero / 2)
print(f"novalista = {novalista}")





for x in range(len(lista)):
    if lista[x] > 20:
        lista[x] = lista[x] / 2
print(lista)
