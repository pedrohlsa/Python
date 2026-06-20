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

# Usando *args com parâmetros normais
def minha_funcao(normal, *args):
    print(f"Normal: {normal}")
    print(f"Args: {args}")

minha_funcao("primeiro", 1, 2, 3)
# Normal: primeiro
# Args: (1, 2, 3)

# Usando **kwargs com parâmetros normais
def minha_funcao(normal, **kwargs):
    print(f"Normal: {normal}")
    print(f"Kwargs: {kwargs}")

minha_funcao("primeiro", nome="João", idade=30)
# Normal: primeiro
# Kwargs: {'nome': 'João', 'idade': 30}

# *args e **kwargs juntos com parâmetros normais
def minha_funcao(normal, *args, **kwargs):
    print(f"Normal: {normal}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

minha_funcao("primeiro", 1, 2, 3, nome="João", idade=30)
# Normal: primeiro
# Args: (1, 2, 3)
# Kwargs: {'nome': 'João', 'idade': 30}

# Exemplo prático: função flexível de saudação
def saudacao(saudacao_padrao="Olá", *nomes, **detalhes):
    for nome in nomes:
        print(f"{saudacao_padrao}, {nome}!")
    for key, value in detalhes.items():
        print(f"{key}: {value}")

saudacao("Oi", "João", "Maria", "Pedro", cidade="SP", idade=25)
# Oi, João!
# Oi, Maria!
# Oi, Pedro!
# cidade: SP
# idade: 25
