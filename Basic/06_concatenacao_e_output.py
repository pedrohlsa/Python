x = "Python"
y = "is"
z = "Awesome"

# Jeito 1: vírgula (com espaços)
print(x, z, y)

# Jeito 2: + (sem espaços)
print(x + z + y)

# Jeito 3: f-strings (RECOMENDADO)
print(f"{x} {z} {y}")

# CUIDADO: int + str dá erro
x = "John"
y = 5
print(x, y)  # Correto
print(f"{x} {y}")  # Correto
