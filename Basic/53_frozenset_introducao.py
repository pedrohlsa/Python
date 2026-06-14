# FROZENSET - versão IMUTÁVEL do set
# Não pode adicionar, remover ou modificar elementos

# Criando frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))  # <class 'frozenset'>

# Características:
# - UNIQUE (sem duplicatas)
# - UNORDERED (desordenado)
# - UNCHANGEABLE (imutável - não pode adicionar/remover)

# Métodos disponíveis (só leitura):
# - copy()
# - difference()
# - intersection()
# - isdisjoint()
# - issubset()
# - issuperset()
# - symmetric_difference()
# - union()

# Exemplo de uso:
A = frozenset({1, 2, 3, 4})
B = frozenset({3, 4, 5, 6})

# Pode fazer operações normalmente (retornam novos frozensets)
print(A.union(B))       # frozenset({1, 2, 3, 4, 5, 6})
print(A.intersection(B)) # frozenset({3, 4})
print(A.difference(B))   # frozenset({1, 2})

# NÃO pode modificar
# A.add(5)     # AttributeError! 'frozenset' object has no attribute 'add'
# A.remove(1)  # AttributeError!
