# Operadores Lógicos: and, or, not

x = 5

# and: True se AMBOS forem True
print(x > 0 and x < 10)   # True (5>0 e 5<10)

# or: True se PELO MENOS UM for True
print(x < 5 or x > 10)    # False (nenhuma condição é True)

# not: inverte o resultado
print(not(x > 3 and x < 10))  # False (inverteu o True)

# Tabela verdade
print("\n--- Tabela AND ---")
print(f"True and True: {True and True}")     # True
print(f"True and False: {True and False}")   # False
print(f"False and True: {False and True}")   # False
print(f"False and False: {False and False}") # False

print("\n--- Tabela OR ---")
print(f"True or True: {True or True}")       # True
print(f"True or False: {True or False}")     # True
print(f"False or True: {False or True}")     # True
print(f"False or False: {False or False}")   # False
