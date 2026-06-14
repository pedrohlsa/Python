# DIFERENÇA SIMÉTRICA - itens que NÃO estão em AMBOS (tira as duplicatas)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# symmetric_difference() - retorna NOVO set
set3 = set1.symmetric_difference(set2)
print(set3)  # {'banana', 'cherry', 'google', 'microsoft'}

# Operador ^ - mesma coisa
set3 = set1 ^ set2
print(set3)  # {'banana', 'cherry', 'google', 'microsoft'}

# symmetric_difference_update() - modifica o set original
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)  # modifica set1
print(set1)  # {'banana', 'cherry', 'google', 'microsoft'}

# Visualizando a diferença:
# set1: {apple, banana, cherry}
# set2: {google, microsoft, apple}
# 
# Itens em COMUM: apple (vai ser removido)
# Itens DIFERENTES: banana, cherry, google, microsoft (fica só esses)
