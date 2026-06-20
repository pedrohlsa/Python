# NESTED IF - If dentro de if

# Exemplo 1: básico
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("And also above 20!")
    else:
        print("but not above 20.")

# Exemplo 2: carteira de motorista
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

# Exemplo 3: múltiplos níveis
score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

# Exemplo 4: login com validação
username = "Emil"
password = "python123"
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password Required")
else:
    print("Username required")

# Nested if vs AND (qual usar?)
temperature = 25
is_sunny = True

# Jeito 1: nested if
if temperature > 20:
    if is_sunny:
        print("Perfect beach weather")

# Jeito 2: AND (mais simples)
if temperature > 20 and is_sunny:
    print("Perfect beach weather")

# REGRA: use AND quando as condições são SIMPLES e INDEPENDENTES
# Use nested if quando a lógica interna é COMPLEXA ou DEPENDE da condição externa
