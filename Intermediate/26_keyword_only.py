# KEYWORD-ONLY - Argumentos SÓ por nome (usando *)

# Tudo DEPOIS do * é keyword-only
def my_function(*, name):
    print("Hello", name)

# Só funciona com keyword
# my_function("Emil")        # ❌ TypeError!
my_function(name="Emil")    # ✅ Hello Emil

# Múltiplos argumentos keyword-only
def minha_funcao(*, a, b, c):
    print(a, b, c)

minha_funcao(a=1, b=2, c=3)  # ✅
# minha_funcao(1, 2, 3)      # ❌ TypeError!

# Misturando: antes do * é normal, depois é keyword-only
def minha_funcao(a, b, *, c, d):
    print(a, b, c, d)

minha_funcao(1, 2, c=3, d=4)    # ✅
# minha_funcao(1, 2, 3, 4)      # ❌ (c e d são keyword-only)

# Combinando position-only e keyword-only
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c=15, d=20)
print(result)  # 50
