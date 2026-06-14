# SETS - unordered, unchangeable*, no duplicates

myset = {"apple", "banana", "cherry"}
print(myset)

# Características:
# - UNORDERED: não tem ordem definida (pode mudar a cada execução)
# - UNCHANGEABLE*: não pode mudar itens, mas pode adicionar/remover
# - NO DUPLICATES: não permite valores repetidos

# Duplicatas são ignoradas
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # {'apple', 'banana', 'cherry'}

# True e 1 são considerados iguais
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  # {True, 2, 'apple', 'banana', 'cherry'}

# False e 0 são considerados iguais
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)  # {False, True, 'apple', 'banana', 'cherry'}

# len()
print(len(thisset))

# Pode ter tipos diferentes
set1 = {"abc", 34, True, 40, "male"}

# Construtor set()
thisset = set(("apple", "banana", "cherry"))
print(thisset)

# Loop em set (única forma de acessar itens)
for x in thisset:
    print(x)

# Verificar existência
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)      # True
print("banana" not in thisset)  # False
