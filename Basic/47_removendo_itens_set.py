# REMOVENDO ITENS EM SETS

thisset = {"apple", "banana", "cherry"}

# remove() - remove item (dá erro se não existir)
thisset.remove("banana")
print(thisset)

# discard() - remove item (NÃO dá erro se não existir)
thisset.discard("banana")  # não existe, mas não dá erro
print(thisset)

# pop() - remove um item ALEATÓRIO (sets são desordenados)
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # não sabe qual item vai sair
print(f"Item removido: {x}")
print(thisset)

# clear() - limpa todos os itens (set vazio)
thisset.clear()
print(thisset)  # set()

# del - deleta completamente o set
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)  # NameError: name 'thisset' is not defined
