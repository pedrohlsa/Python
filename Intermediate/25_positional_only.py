# POSITIONAL-ONLY - Argumentos SÓ por posição (usando /)

# Tudo ANTES do / é posicional
def my_function(name, /):
    print("Hello", name)

# Só funciona com posicional
my_function("Emil")        # ✅ Hello Emil
# my_function(name="Emil")  # ❌ TypeError!

# Múltiplos argumentos posicionais
def dividir(dividendo, divisor, /):
    return dividendo / divisor

print(dividir(10, 2))  # 5.0
# print(dividir(dividendo=10, divisor=2))  # ❌ TypeError!

# Misturando: antes do / é posicional, depois pode ser qualquer
def minha_funcao(a, b, /, c, d):
    print(a, b, c, d)

minha_funcao(1, 2, 3, 4)        # ✅
minha_funcao(1, 2, c=3, d=4)    # ✅
# minha_funcao(a=1, b=2, c=3, d=4)  # ❌ (a e b são posicionais)
