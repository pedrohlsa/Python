# INTERSEÇÃO - mantém APENAS os DUPLICADOS (itens que estão em AMBOS)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "cherry"}

# intersection() - retorna NOVO set com duplicatas
set3 = set1.intersection(set2)
print(set3)  # {'cherry'}

# Operador & - mesma coisa
set3 = set1 & set2
print(set3)  # {'cherry'}

# intersection_update() - modifica o set original (não retorna novo)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)  # {'apple'}

# ATENÇÃO: True/False e 1/0 são considerados iguais!
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set2.intersection(set1)
print(set3)  # {1, 'apple'}  (True e 1 são iguais, False e 0 também)
