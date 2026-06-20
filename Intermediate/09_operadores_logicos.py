# OPERADORES LÓGICOS: and, or, not

# AND - True se AMBOS forem True
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

# OR - True se PELO MENOS UM for True
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one condition is True")

# NOT - Inverte o resultado
a = 33
b = 200

if not a > b:
    print("a is NOT greater than b")  # True

# Tabela verdade
print("\n--- AND ---")
print(f"True and True: {True and True}")     # True
print(f"True and False: {True and False}")   # False

print("\n--- OR ---")
print(f"True or False: {True or False}")     # True
print(f"False or False: {False or False}")   # False

print("\n--- NOT ---")
print(f"not True: {not True}")    # False
print(f"not False: {not False}")  # True
