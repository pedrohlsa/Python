# DICIONÁRIOS - key:value pairs

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# Características:
# - ORDERED (tem ordem definida - Python 3.7+)
# - CHANGEABLE (mutável, pode alterar)
# - NO DUPLICATES (não permite chaves duplicadas)

# Acessar pelo nome da chave
print(thisdict["brand"])  # Ford

# len() - tamanho
print(len(thisdict))  # 3

# Valores podem ser de qualquer tipo
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(type(thisdict))  # <class 'dict'>

# Construtor dict()
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)  # {'name': 'John', 'age': 36, 'country': 'Norway'}

# RESUMO DAS COLEÇÕES:
# LIST: ordered, changeable, duplicate OK
# TUPLE: ordered, unchangeable, duplicate OK
# SET: unordered, unchangeable*, unindexed, duplicate NO
# DICT: ordered**, changeable, duplicate NO (chaves)
