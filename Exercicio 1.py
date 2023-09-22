"""
Aritmético
"""

def aritmetica(op, n1, n2):
    if op == '+':
        resultado = n1 + n2
    elif op == '-':
        resultado = n1 + n2
    elif op == '*':
        resultado = n1 * n2
    elif op == '/':
        resultado = n1 / n2
    else:
        resultado = 'Operação inválida'
    return resultado

def contas(op, n1, n2):
    if op == '+':
        resultado = n1 + n2
    else:
        if op == '-':
            resultado = n1 - n2
        else:
            if op == '*':
                resultado = n1 * n2
            else:
                if op == '/':
                    resultado = n1 / n2
                else:
                    resultado = 'Operação inválida'
    return resultado



def continhas(op, n1 , n2):
    resultado = 'Operação inválida'
    if op == '+':
        resultado = n1 + n2
    if op == '-':
        resultado = n1 - n2
    if op == '*':
        resultado = n1 * n2
    if op == '/':
        resultado = n1 / n2
    print(type(op))
    print(f"O type de op é {type(op)}")
    print(f"O type de 'n1' é {type(n1)}")
    return resultado



print(aritmetica('+', 20, 3))
print(aritmetica('-', 20, 3))
print(aritmetica('*', 20, 3))
print(aritmetica('/', 20, 3))
print(aritmetica('bla', 20, 3))
print('-----')
print(contas('+', 20, 3))
print(contas('-', 20, 3))
print(contas('*', 20, 3))
print(contas('/', 20, 3))
print(contas('bla', 20, 3))
print('-----')
print(continhas('+', 20, 3))
print(continhas('-', 20, 3))
print(continhas('*', 20, 3))
print(continhas('/', 20, 3))
print(continhas('bla', 20, 3))