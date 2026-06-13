# Operadores de Comparação
# Sempre retornam True ou False

x = 5
y = 3

print(f"x == y: {x == y}")  # Igual -> False
print(f"x != y: {x != y}")  # Diferente -> True
print(f"x > y:  {x > y}")   # Maior -> True
print(f"x < y:  {x < y}")   # Menor -> False
print(f"x >= y: {x >= y}")  # Maior ou igual -> True
print(f"x <= y: {x <= y}")  # Menor ou igual -> False

# Chaining (encadeamento)
x = 5
print(1 < x < 10)        # True (5 está entre 1 e 10)
print(1 < x and x < 10)  # Mesma coisa que acima
