ilhas = ['pico', 'terceira', 'graciosa', 'faial', 'saojorge']
vendas = [0, 0, 0, 0, 0]
total = 0

for i in range(len(ilhas)):
    print(f'Insira as vendas para {ilhas[i]}:')
    vendas[i] = int(input())
    total += vendas[i]

valormáximo = max(vendas)
valormínimo = min(vendas)

print(f"O total de vendas é de {total}")
print(f"O valor mínimo de vendas é {valormínimo} na ilha {ilha_mínimo}")
print(f"O valor máximo de vendas é {valormáximo} na ilha {ilha_máximo}")

