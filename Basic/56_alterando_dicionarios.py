# ALTERANDO DICIONÁRIOS

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# Jeito 1: colchetes
thisdict["year"] = 2018
print(thisdict["year"])  # 2018

# Jeito 2: update() (RECOMENDADO)
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})
print(thisdict["year"])  # 2020

# update() também funciona com outro dicionário
novos_dados = {"year": 2022, "color": "red"}
thisdict.update(novos_dados)
print(thisdict)  # brand, model, year 2022, color red
