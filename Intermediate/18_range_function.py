# RANGE() - Gera sequência de números

# range(stop) - de 0 até stop-1
for x in range(6):
    print(x)  # 0, 1, 2, 3, 4, 5

# range(start, stop) - de start até stop-1
for x in range(2, 6):
    print(x)  # 2, 3, 4, 5

# range(start, stop, step) - com incremento
for x in range(2, 30, 3):
    print(x)  # 2, 5, 8, 11, 14, 17, 20, 23, 26, 29

# range com step negativo (contagem regressiva)
for x in range(10, 0, -2):
    print(x)  # 10, 8, 6, 4, 2

# range não é uma lista, é um objeto iterável
print(range(5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]
