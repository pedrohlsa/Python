txt = "Hello World"

# capitalize() - Primeira letra maiúscula, resto minúscula
print(txt.capitalize())  # Hello world

# casefold() - Versão mais agressiva do lower() (para comparações)
print(txt.casefold())  # hello world

# center() - Centraliza com espaços ao redor
print(txt.center(50))  # "                  Hello World                   "

# endswith() - Verifica se termina com algo
print(txt.endswith('d'))   # True
print(txt.endswith('World')) # True

# find() - Retorna posição onde encontra o texto
print(txt.find('W'))  # 6 (índice onde 'W' começa)
print(txt.find('x'))  # -1 (não encontrou)

# join() - Junta itens com um separador
print("-".join(txt))  # H-e-l-l-o- -W-o-r-l-d
print(", ".join(["maçã", "banana", "laranja"]))  # maçã, banana, laranja

# replace() - Substitui texto
print(txt.replace("World", "Python"))  # Hello Python

# split() já vimos
print(txt.split())  # ['Hello', 'World']
