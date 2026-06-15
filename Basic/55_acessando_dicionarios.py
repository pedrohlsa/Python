# ACESSANDO DICIONÁRIOS

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# Jeito 1: colchetes com o nome da chave
x = thisdict["model"]
print(x)  # Mustang

# Jeito 2: método get()
x = thisdict.get("model")
print(x)  # Mustang

# keys() - retorna todas as chaves
x = thisdict.keys()
print(x)  # dict_keys(['brand', 'model', 'year', 'colors'])

# keys() é uma VIEW - se o dicionário mudar, x muda também
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)  # before: dict_keys(['brand', 'model', 'year'])

car["color"] = "white"
print(x)  # after: dict_keys(['brand', 'model', 'year', 'color'])

# values() - retorna todos os valores
x = car.values()
print(x)  # dict_values(['Ford', 'Mustang', 1964, 'white'])

# items() - retorna pares (chave, valor) como tuplas
x = thisdict.items()
print(x)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ...])

# Verificar se chave existe
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
    print("Yes, 'model' is in this dictionary")
