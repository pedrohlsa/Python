# bool() - Função que avalia qualquer valor

# VALORES QUE RETORNAM True
print(bool("Hello"))   # True (string não vazia)
print(bool(15))        # True (número não zero)
print(bool(["a", "b"])) # True (lista não vazia)

# VALORES QUE RETORNAM False
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False (string vazia)
print(bool(()))     # False (tupla vazia)
print(bool([]))     # False (lista vazia)
print(bool({}))     # False (dicionário vazio)

# REGRA: A MAIORIA dos valores são True
# Exceções: 0, None, False, coleções vazias, strings vazias
