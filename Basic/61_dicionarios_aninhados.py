# DICIONÁRIOS ANINHADOS (nested dictionaries)

# Jeito 1: criar direto
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

# Jeito 2: criar separado e depois juntar
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# Acessar item em dicionário aninhado
print(myfamily["child2"]["name"])  # Tobias

# Loop em dicionário aninhado
for x, obj in myfamily.items():
    print(f"\n{x}:")
    for y in obj:
        print(f"  {y}: {obj[y]}")
