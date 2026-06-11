# FORMA ERRADA (dá TypeError)
age = 36
# txt = "My name is John, i am" + age  # ❌ NÃO FAÇA ISSO!

# FORMA CERTA (f-string) - RECOMENDADA
age = 36
txt = f"My name is John, I am {age}"
print(txt)  # My name is John, I am 36

# Múltiplas variáveis
nome = "John"
idade = 36
cidade = "New York"
msg = f"{nome} tem {idade} anos e mora em {cidade}"
print(msg)
