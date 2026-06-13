# REMOVENDO ITENS DE LISTAS

# remove() - remove pela VALOR (primeira ocorrência)
thislist = ["apple", "banana", "cherry", "banana"]
thislist.remove("banana")
print(thislist)  # ['apple', 'cherry', 'banana']

# pop() - remove por ÍNDICE (se não passar, remove o último)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # remove índice 1 ("banana")
print(thislist)  # ['apple', 'cherry']

thislist.pop()  # remove último
print(thislist)  # ['apple']

# del - deleta por índice ou deleta a lista inteira
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # ['banana', 'cherry']

# del thislist  # descomentar apaga a lista inteira

# clear() - esvazia a lista (mas mantém o objeto)
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # []
