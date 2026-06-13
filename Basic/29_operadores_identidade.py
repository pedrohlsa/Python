# Operadores de Identidade: is / is not
# Verificam se apontam para o MESMO objeto na memória

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x  # z aponta pro mesmo objeto que x

print(f"x is z: {x is z}")     # True (mesmo objeto)
print(f"x is y: {x is y}")     # False (objetos diferentes)
print(f"x == y: {x == y}")     # True (mesmo VALOR)

# Diferença entre is e ==
print("\n--- DIFERENÇA ---")
print(f"x is y: {x is y}")     # False (objetos diferentes)
print(f"x == y: {x == y}")     # True (valores iguais)

# is not (oposto)
print(f"\nx is not y: {x is not y}")  # True

# Exemplo com números (atenção: Python pode reutilizar objetos)
a = 5
b = 5
print(f"\na is b: {a is b}")  # True (Python reusa ints pequenos)
