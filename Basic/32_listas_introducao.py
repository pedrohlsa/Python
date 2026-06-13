# LISTAS em Python

# Criando listas
thislist = ["apple", "banana", "cherry"]
print(thislist)  # ['apple', 'banana', 'cherry']

# Características das listas:
# - ORDERNADAS (mantém a ordem dos elementos)
# - CHANGEABLE (mutáveis, pode alterar)
# - Permite valores DUPLICADOS

lista_com_duplicatas = ["apple", "banana", "cherry", "apple", "cherry"]
print(lista_com_duplicatas)

# Adicionar itens (mantém ordem - novo vai pro final)
lista_com_duplicatas += ["billy"]
print(lista_com_duplicatas)

# len() - tamanho da lista
print(f"Tamanho: {len(lista_com_duplicatas)}")

# Listas podem ter tipos diferentes
lista_mista = ["abc", 34, True, 40, "male"]
print(lista_mista)
print(type(lista_mista))  # <class 'list'>

# Construtor list()
construtor_lista = list(("apple", "banana", "cherry"))  # double parentheses
print(construtor_lista)

# Tipos de coleções em Python:
# LIST: ordered, changeable, duplicate OK
# TUPLE: ordered, unchangeable, duplicate OK
# SET: unordered, unchangeable*, unindexed, duplicate NOT OK
# DICT: ordered**, changeable, duplicate NOT OK
