# DIFERENÇA - itens do PRIMEIRO set que NÃO estão no segundo

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# difference() - retorna NOVO set
set3 = set1.difference(set2)  # o que tem em set1 que não tem em set2
print(set3)  # {'banana', 'cherry'}

# Operador - (menos) - só funciona entre sets
set3 = set1 - set2
print(set3)  # {'banana', 'cherry'}

# difference_update() - modifica o set original
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)  # remove de set1 o que tem em set2
print(set1)  # {'banana', 'cherry'}

# Exemplo prático
alunos_totais = {"João", "Maria", "José", "Ana"}
alunos_presentes = {"João", "Maria"}

alunos_ausentes = alunos_totais.difference(alunos_presentes)
print(f"Ausentes: {alunos_ausentes}")  # {'José', 'Ana'}
