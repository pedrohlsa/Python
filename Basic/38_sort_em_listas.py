# SORT em listas

# sort() - ordena por padrão (alfabético A-Z, numérico menor-maior)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  # [23, 50, 65, 82, 100]

# Ordem decrescente (reverse=True)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)  # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)  # [100, 82, 65, 50, 23]

# Função personalizada (key)
def myfunc(n):
    return abs(n - 50)  # quão longe está de 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)  # [50, 65, 23, 82, 100]

# Case-sensitive (maiúsculas vêm antes)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)  # ['Kiwi', 'Orange', 'banana', 'cherry']

# Ignorar case
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)  # ['banana', 'cherry', 'Kiwi', 'Orange']

# reverse() - inverte a ordem (não ordena, só inverte)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)  # ['cherry', 'Kiwi', 'Orange', 'banana']
