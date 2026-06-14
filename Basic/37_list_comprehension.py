# LIST COMPREHENSION - Jeito mais curto de criar listas

# JEITO NORMAL (sem comprehension)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)  # ['apple', 'banana', 'manga']

# JEITO COMPREHENSION (curto e elegante)
newlist = [x for x in fruits if "a" in x]
print(newlist)  # ['apple', 'banana', 'mango']

# SINTAXE:
# newlist = [expression for item in iterable if condition == True]

# Exemplos:

# Sem condition (só copiar)
newlist = [x for x in fruits]
print(newlist)  # ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Com condition (filtra)
newlist = [x for x in fruits if x != "apple"]
print(newlist)  # ['banana', 'cherry', 'kiwi', 'mango']

# Com range
newlist = [x for x in range(10)]
print(newlist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Com range e condition
newlist = [x for x in range(10) if x < 5]
print(newlist)  # [0, 1, 2, 3, 4]

# Transformando valores
newlist = [x.upper() for x in fruits]
print(newlist)  # ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# Colocando valor fixo
newlist = ['billy' for x in fruits]
print(newlist)  # ['billy', 'billy', 'billy', 'billy', 'billy']

# Expressão com if/else (diferente do filter)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # ['apple', 'orange', 'cherry', 'kiwi', 'mango']
