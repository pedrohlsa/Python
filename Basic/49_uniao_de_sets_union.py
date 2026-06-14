# UNIÃO de sets - junta TODOS os itens (sem duplicatas)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# Método union() - retorna um NOVO set
set3 = set1.union(set2)
print(set3)  # {1, 2, 3, 'a', 'b', 'c'}

# Operador | - mesma coisa
set3 = set1 | set2
print(set3)

# Unir MÚLTIPLOS sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# Union com outros iteráveis (lista, tupla)
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)  # union aceita qualquer iterável
print(z)  # {1, 2, 3, 'a', 'b', 'c'}

# update() - insere itens em OUTRO set (modifica o original)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)  # modifica set1 diretamente
print(set1)  # {1, 2, 3, 'a', 'b', 'c'}

# | operador SÓ funciona com sets
# set1 | y  # Isso daria erro se y não for set
