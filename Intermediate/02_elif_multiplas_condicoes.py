# ELIF - Múltiplas condições

# elif = "se a condição anterior não for True, tenta essa"

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Múltiplos elif (Python avalia de cima pra baixo)
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Exemplo com idade
age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

# IMPORTANTE: Python para no PRIMEIRO True que encontrar
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")  # <-- executa esse e PARA
elif day == 4:
    print("Thursday")   # <-- esse NÃO executa
