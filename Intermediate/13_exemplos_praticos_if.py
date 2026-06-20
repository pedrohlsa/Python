# EXEMPLOS PRÁTICOS DE IF/ELSE

# 1. Calculadora de nota com extra credit
score = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:
    if extra_credit > 5:
        print("B+ grade")
    else:
        print("B grade")
else:
    print("C grade or below")

# 2. Classificador de idade
age = 25

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# 3. Validação de dados
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if nome and idade > 0:
    if idade >= 18:
        print(f"{nome}, você é maior de idade")
    else:
        print(f"{nome}, você é menor de idade")
else:
    print("Dados inválidos")

# 4. Desconto progressivo
valor_compra = 150
cliente_vip = True

if valor_compra > 100 and cliente_vip:
    desconto = 0.20
elif valor_compra > 100:
    desconto = 0.10
elif cliente_vip:
    desconto = 0.05
else:
    desconto = 0

print(f"Desconto: {desconto * 100}%")
