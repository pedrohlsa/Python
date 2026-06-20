# RETURN - Retorna valor da função

# Retornando string
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

# Retornando direto
def get_greeting():
    return "Hello from a function"

print(get_greeting())  # Hello from a function

# Se não tem return, retorna None
def sem_return():
    print("Não retorna nada")

resultado = sem_return()
print(resultado)  # None

# Retornando número
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)  # 8

# Retornando lista
def get_fruits():
    return ["apple", "banana", "cherry"]

fruits = get_fruits()
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[2])  # cherry

# Retornando tupla (unpacking)
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print("x:", x)  # x: 10
print("y:", y)  # y: 20
