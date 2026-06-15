# COPIANDO DICIONÁRIOS

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Jeito 1: copy() (RECOMENDADO)
mydict = thisdict.copy()
print(mydict)

# Jeito 2: dict() construtor
mydict = dict(thisdict)
print(mydict)

# ATENÇÃO: isso NÃO é uma cópia!
# mydict = thisdict  # mydict vira referência, não cópia!
