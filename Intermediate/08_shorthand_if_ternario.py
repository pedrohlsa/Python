# SHORTHAND IF - Uma linha só

a = 5
b = 2

# if em uma linha
if a > b: print("a is greater than b")

# Shorthand if/else (ternário)
a = 5
b = 2
print("A") if a > b else print("B")

# Ternário com atribuição (mais útil)
a = 10
b = 20

# Sintaxe: valor_se_true if condicao else valor_se_false
maior = a if a > b else b
print(f"Maior é {maior}")

# Múltiplas condições em uma linha (elif encadeado)
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Exemplo prático: valor máximo
x = 15
y = 20
max_value = x if x > y else y
print(f"Maximum Value: {max_value}")

# Valor padrão com ternário
username = ""
display_name = username if username else "Guest"
print(f"Welcome, {display_name}")  # Welcome, Guest

# ⚠️ ATENÇÃO: use ternário SÓ quando for SIMPLES
# Se for complexo, usa if/else normal
