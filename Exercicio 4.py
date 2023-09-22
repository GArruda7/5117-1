"""
Quantos numeros é que há entre eles?
"""

lista = [10, 20, 20, 15, 5, 60, 140, 80, 20, 20, 15, 5, 60, 140]

n10 = 0
n20 = 0
n30 = 0
n40 = 0
n50 = 0
n5x = 0

for num in lista:
    if num <= 10:
        n10 += 1
    elif num <= 20:
        n20 += 1
    elif num <= 30:
        n30 += 1
    elif num <= 40:
        n40 += 1
    elif num <= 50:
        n50 += 1

print(f"n10 = {n10}")
print(f"n20 = {n20}")
print(f"n30 = {n30}")
print(f"n40 = {n40}")
print(f"n50 = {n50}")
