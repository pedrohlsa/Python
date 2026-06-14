# ACESSANDO itens de tuplas (igual listas)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# Índice positivo
print(thistuple[1])    # banana
print(thistuple[2])    # cherry

# Índice negativo
print(thistuple[-1])   # mango (último)
print(thistuple[-2])   # melon

# Slicing [inicio:fim] (fim não incluso)
print(thistuple[2:5])  # ('cherry', 'orange', 'kiwi')
print(thistuple[:4])   # ('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:])   # ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Slicing com negativo
print(thistuple[-4:-1])  # ('orange', 'kiwi', 'melon')

# Verificar se existe
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
