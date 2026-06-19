# TRUTHY e FALSEY - O que é considerado True/False

# FALSEY (tudo isso é considerado False):
print(bool(0))          # False
print(bool(""))         # False (string vazia)
print(bool(None))       # False
print(bool([]))         # False (lista vazia)
print(bool(()))         # False (tupla vazia)
print(bool({}))         # False (dicionário vazio)
print(bool(False))      # False

# TRUTHY (qualquer coisa diferente disso é True):
print(bool(1))          # True
print(bool(-1))         # True
print(bool("Hello"))    # True
print(bool([1, 2]))     # True
print(bool({"a": 1}))   # True

# Usando no if (MUITO COMUM)
nome = input("Digite seu nome: ")
if nome:  # se não for string vazia
    print(f"Olá, {nome}!")
else:
    print("Você não digitou nada!")

# Outro exemplo
lista = []
if lista:  # se lista NÃO estiver vazia
    print(f"Lista tem {len(lista)} itens")
else:
    print("Lista vazia")
