# ADICIONANDO itens em sets

# add() - adiciona um item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  # {'orange', 'banana', 'cherry', 'apple'}

# update() - adiciona vários itens (de qualquer iterável)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  # {'papaya', 'cherry', 'mango', 'banana', 'pineapple', 'apple'}

# update com lista
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)  # {'orange', 'cherry', 'banana', 'kiwi', 'apple'}

# update com tupla
thisset = {"apple", "banana", "cherry"}
mytuple = ("kiwi", "orange")
thisset.update(mytuple)
print(thisset)

# remove() - remove item (dá erro se não existir)
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # {'cherry', 'apple'}

# discard() - remove item (NÃO dá erro se não existir)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
thisset.discard("morango")  # não existe, mas não dá erro
print(thisset)

# pop() - remove um item ALEATÓRIO (cuidado!)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # não sabe qual vai sair
print(x)
print(thisset)

# clear() - limpa o set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # set()

# del - deleta o set
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)  # NameError
