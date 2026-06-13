# Operador Ternário (condição em uma linha)

# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso

num = 6
x = "Weekend" if num > 5 else "Workday"
print(x)  # Weekend (6 > 5)

# Com elif (encadeado)
num = 6
x = ("Fri" if num == 5 else 
     "Sat" if num == 6 else 
     "Sun" if num == 7 else 
     "Weekday")
print(x)  # Sat

# Exemplo prático
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)  # Maior de idade
