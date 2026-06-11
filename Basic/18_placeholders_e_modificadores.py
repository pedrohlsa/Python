# MODIFICADOR :.2f (2 casas decimais)
price = 59
txt = f"Price is {price:.2f} dollars"
print(txt)  # Price is 59.00 dollars

# Outros modificadores úteis
num = 10.56789
print(f"{num:.1f}")   # 10.6 (1 casa)
print(f"{num:.3f}")   # 10.568 (3 casas)

# Placeholder pode conter operações matemáticas
txt = f"The price is {20 * 59} dollars"
print(txt)  # The price is 1180 dollars

# Pode chamar funções dentro das chaves
print(f"{'hello'.upper()}")  # HELLO
