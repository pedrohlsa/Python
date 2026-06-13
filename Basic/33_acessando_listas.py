# ACESSANDO ITENS DE LISTAS

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Índice positivo (começa no 0)
print(thislist[0])  # apple
print(thislist[1])  # banana
print(thislist[2])  # cherry

# Índice negativo (começa do final)
print(thislist[-1])  # mango (último)
print(thislist[-2])  # melon (penúltimo)

# Slicing [inicio:fim] (fim NÃO é incluído)
print(thislist[2:5])   # ['cherry', 'orange', 'kiwi']
print(thislist[:4])    # ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])    # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# Slicing com índices negativos
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon'] (-1 = mango, não incluído)

# Verificar se item existe
fruta_busca = "banana"
if fruta_busca in thislist:
    print(f"{fruta_busca} está na lista!")

# Usando input (igual você fez!)
if (variavel := input("What fruit do you want to find? ")) in thislist:
    print(f"Yes, {variavel} is in this list")
else:
    print(f"No, {variavel} is not in this list")
