res = [0, 0, 0, 0, 0, 0]

for num in res:
    if num <= 10:
        res[0] += 1
    elif num <= 20:
        res[1] += 1
    elif num <= 30:
        res[2] += 1
    elif num <= 40:
        res[3] += 1
    elif num <= 50:
        res[4] += 1
    else:
        res [5] += 1

for x in range(0, len(res)):
    print(f"rest[{x}] = {res[x]}")

