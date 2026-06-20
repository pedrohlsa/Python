# COMBINANDO OPERADORES LÓGICOS

# Exemplo 1: múltiplas condições
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")

# Exemplo 2: com parênteses (mais legível)
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")

# Exemplo 3: validação de login
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    print("Login Successful!")
else:
    print("Login Failed")

# Exemplo 4: validação de score
score = 85

if score >= 0 and score <= 100:
    print("Valid Score")
else:
    print("Invalid Score")

# REGRA: use parênteses pra deixar claro a ordem
# NOT > AND > OR (ordem de precedência)
