# TUPLAS - ordered, unchangeable, allow duplicates

mytuple = ("apple", "banana", "cherry")
print(mytuple)

# Características:
# - ORDERED: tem ordem definida
# - UNCHANGEABLE: NÃO pode mudar, adicionar ou remover (criada e já era)
# - ALLOW DUPLICATES: pode ter valores repetidos

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)  # ('apple', 'banana', 'cherry', 'apple', 'cherry')

# len() - tamanho
print(len(thistuple))  # 5

# Tupla com UM item (precisa da vírgula!)
thistuple = ("apple",)  # ✅ É tupla
print(type(thistuple))

thistuple = ("apple")   # ❌ É string!
print(type(thistuple))  # <class 'str'>

# Pode ter tipos diferentes
tuple1 = ("abc", 34, True, 40, "male")

# Construtor tuple()
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
