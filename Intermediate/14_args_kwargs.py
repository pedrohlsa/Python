# *args e **kwargs - Argumentos arbitrários

# *args = Argumentos posicionais (vira tupla)
# **kwargs = Argumentos nomeados (vira dicionário)

# Exemplo básico de *args
def minha_funcao(*args):
    for arg in args:
        print(arg)

minha_funcao("apple", "banana", "cherry")
# apple
# banana
# cherry

# Exemplo básico de **kwargs
def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

minha_funcao(nome="João", idade=30, cidade="SP")
# nome: João
# idade: 30
# cidade: SP

# Combinando os dois
def minha_funcao(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

minha_funcao(1, 2, 3, x=10, y=20)
# Args: (1, 2, 3)
# Kwargs: {'x': 10, 'y': 20}
