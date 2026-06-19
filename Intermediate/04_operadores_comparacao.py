# OPERADORES DE COMPARAÇÃO (usados em if/else)

# ==   igual
# !=   diferente
# >    maior que
# <    menor que
# >=   maior ou igual
# <=   menor ou igual

a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# Usando em if
idade = 18
if idade >= 18:
    print("Pode votar")

# Comparando strings (case sensitive)
nome = "João"
if nome == "João":
    print("É o João")

# Comparando diferentes tipos
if 10 == 10.0:   # True (Python converte)
    print("São iguais")
