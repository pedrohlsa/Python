# LOOP EM DICIONÁRIOS

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Printar todas as CHAVES
print("--- CHAVES ---")
for x in thisdict:
    print(x)  # brand, model, year

# Printar todos os VALORES (jeito 1)
print("--- VALORES (jeito 1) ---")
for x in thisdict:
    print(thisdict[x])

# Printar todos os VALORES (jeito 2 - values())
print("--- VALORES (jeito 2) ---")
for x in thisdict.values():
    print(x)

# Printar todas as CHAVES (jeito 2 - keys())
print("--- CHAVES (jeito 2) ---")
for x in thisdict.keys():
    print(x)

# Printar CHAVE e VALOR juntos (items())
print("--- CHAVE E VALOR ---")
for x, y in thisdict.items():
    print(x, y)  # brand Ford, model Mustang, year 1964
