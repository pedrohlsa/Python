# WHILE LOOP - Repete enquanto condição for True

# Básico
i = 1
while i < 6:
    print(i)
    i += 1

# Com break (para o loop)
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Com continue (pula iteração)
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)  # 1, 2, 4, 5, 6

# Com else (executa quando condição fica False)
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
