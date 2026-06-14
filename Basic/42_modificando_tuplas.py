# MODIFICANDO tuplas - NÃO dá pra modificar direto!
# Mas tem um workaround: converter pra lista, modificar, voltar pra tupla

# Mudar item
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  # ('apple', 'kiwi', 'cherry')

# Adicionar item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)  # ('apple', 'banana', 'cherry', 'orange')

# Adicionar tupla com +=
thistuple = ("apple", "banana", "cherry")
y = ("orange",)  # PRECISA da vírgula!
thistuple += y
print(thistuple)  # ('apple', 'banana', 'cherry', 'orange')

# Remover item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)  # ('banana', 'cherry')

# Deletar tupla inteira
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # NameError: name 'thistuple' is not defined
