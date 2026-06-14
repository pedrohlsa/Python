# COPIANDO e JUNTANDO listas

# COPIANDO listas

# Jeito 1: atribuição direta (NÃO é cópia, é referência)
thislist = ["apple", "banana", "cherry"]
mylist = thislist  # mylist aponta pro MESMO objeto
print(mylist)

# Jeito 2: método list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Jeito 3: slice operator [:])
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# JUNTANDO listas

# Jeito 1: operador +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # ['a', 'b', 'c', 1, 2, 3]

# Jeito 2: append com loop
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# Jeito 3: extend (RECOMENDADO)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# RESUMO DOS MÉTODOS DE LISTA MAIS USADOS:
# append()  - adiciona no final
# clear()   - limpa tudo
# copy()    - copia
# count()   - conta ocorrências
# index()   - acha posição
# insert()  - insere na posição
# pop()     - remove por índice
# remove()  - remove por valor
# reverse() - inverte ordem
# sort()    - ordena
