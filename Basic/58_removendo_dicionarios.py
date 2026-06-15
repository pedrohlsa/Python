# REMOVENDO ITENS DE DICIONÁRIOS

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# pop() - remove pela chave (retorna o valor removido)
thisdict.pop("model")
print(thisdict)  # {'brand': 'Ford', 'year': 1964}

# popitem() - remove o último item (Python 3.7+)
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang'}

# del - remove pela chave
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)  # {'brand': 'Ford', 'year': 1964}

# del thisdict  # isso deletaria o dicionário INTEIRO

# clear() - esvazia o dicionário (mantém o objeto)
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)  # {}
