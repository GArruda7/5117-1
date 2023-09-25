"""
Dias
"""

semanas = [1, 2, 3, 4]
dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta']

x = 0
y = 0
#while x < len(dias):
    #print(dias[x])
    #x += 1

#########################################

while y < len(semanas):
    x = 0
    while x < len(dias):
        print(f'semana: {semanas[y]} - Dia: {dias[x]}')
        x += 1
    y += 1

    print()

#########################################



