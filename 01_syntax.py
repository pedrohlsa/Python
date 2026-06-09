"""
 ============================================================================
 |                    PYTHON FUNDAMENTALS                                   |
 ============================================================================
"""

# ============================================================================
# 1. INDENTAÇÃO (O MAIS IMPORTANTE DO PYTHON)
# ============================================================================

# Python usa indentação pra definir blocos de código
# Padrão: 4 espaços (obrigatório no mínimo 1, mas use SEMPRE 4)

# CORRETO:
if 5 > 2:
    print("Five is greater than two")

# ERRADO (vai dar IndentationError):
# if 5 > 2:
# print("Five is greater than two")  # <-- falta espaços

# REGRA DE OURO: MESMO número de espaços no MESMO bloco
# Isso vale pra if, loops, funções, tudo

# ============================================================================
# 2. PRINT E EXECUÇÃO
# ============================================================================

# Python executa linha por linha, de cima pra baixo
print("Python is fun!")
print("Hello, World!")
print("Hi, World!")

# Ponto e vírgula? Funciona, mas NÃO use (código feio e difícil de ler)
# Certo: cada comando em sua linha
# Errado: print("Hello"); print("How are you?"); print("Bye bye!")

# Print sem quebra de linha 
print("Hello World!", end=" ")
print("I will print on the same line.")
print()  # linha em branco

# Print com números (sem aspas)
print(333334)
print(3 + 3)      # operações matemáticas dentro do print
print("3 + 3")    # texto literal

# Misturando texto e números
print("I am", 35, "years old")  # vírgula adiciona espaço automático

# ============================================================================
# 3. COMENTÁRIOS
# ============================================================================

# Comentário de uma linha

"""
Comentário de múltiplas linhas
Usa 3 aspas
Perfeito pra documentar funções (docstrings)
"""

# Comentário no final da linha é permitido
print("Ok")  # isso é um comentário

# ============================================================================
# 4. VARIÁVEIS 
# ============================================================================

# Python é DINAMICAMENTE TIPADO 
x = 5               # int
y = "Hello, World!" # str

print(x)
print(y)

# Variável pode mudar de tipo a qualquer momento 
x = "Jon"   # agora x é string
y = 4       # agora y é int

# Type casting 
x = str(3)    # "3"
y = int(5)    # 5
z = float(3)  # 3.0

# Verificando o tipo 
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'float'>

# Case-Sensitive: 'a' e 'A' são variáveis diferentes
a = 'John'
A = 'Pork'
print(a)  # John
print(A)  # Pork

# ============================================================================
# 5. REGRAS PARA NOME DE VARIÁVEIS (MUITO PARECIDO COM C)
# ============================================================================

# PODE: letra ou _ no início, letras/números/_, case-sensitive
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"     
MYVAR = "John"      
myvar2 = "John"

# NÃO PODE: começar com número, usar palavras reservadas (if, for, while...)

# ============================================================================
# 6. MÚLTIPLAS ATRIBUIÇÕES 
# ============================================================================

# Atribuição múltipla em uma linha
k, l, y = "Orange", "Banana", "Cherry"

print(k)  # Orange
print(l)  # Banana
print(y)  # Cherry

# Unpacking de listas
fruits = ["Apple", "Pearl", "Juice"]
q, t, r = fruits

print(q)  # Apple
print(t)  # Pearl
print(r)  # Juice

# Todas as variáveis com o mesmo valor
q = t = r = "Apple"

# ============================================================================
# 7. OUTPUT VARIABLES (CONCATENAÇÃO)
# ============================================================================

x = "Python"
y = "is"
z = "Awesome"

# Jeito 1: vírgula (adiciona espaços automaticamente)
print(x, z, y)

# Jeito 2: + (concatena, mas sem espaços)
print(x + z + y)  # PythonisAwesome

# Jeito 3: f-strings 
print(f"{x} {z} {y}")  # Python is Awesome

# CUIDADO: não misture string com int usando +
x = "John"
y = 5
# print(x + y)  # ERRO! TypeError

# Jeito certo:
print(x, y)           # vírgula funciona
print(f"{x} {y}")     # f-string funciona

