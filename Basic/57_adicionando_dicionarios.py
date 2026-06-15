# ADICIONANDO ITENS EM DICIONÁRIOS

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Jeito 1: colchetes com nova chave
thisdict["color"] = "red"
print(thisdict["color"])  # red

# Jeito 2: update() com nova chave
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
