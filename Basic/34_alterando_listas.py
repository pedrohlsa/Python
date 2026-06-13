# ALTERANDO ITENS DE LISTAS

# Mudar um item específico
thislist = ["apple", "banana", "cherry", "kiwi", "morango"]
thislist[1] = "blackcurrant"
print(thislist)  # ['apple', 'blackcurrant', 'cherry', 'kiwi', 'morango']

# Mudar um range de itens
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'kiwi', 'morango']

# Substituir 1 item por 2 itens (a lista aumenta)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# Substituir 2 itens por 1 item (a lista diminui)
thislist[1:3] = ["watermelon"]
print(thislist)  # ['apple', 'watermelon', 'cherry']

# insert() - insere sem substituir (desloca os outros)
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")  # (posição, valor)
print(thislist)  # ['apple', 'banana', 'watermelon', 'cherry']
