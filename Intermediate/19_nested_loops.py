# NESTED LOOPS - Loop dentro de loop

# O loop interno executa COMPLETO para CADA iteração do externo
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# Saída:
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry

# Exemplo prático: tabuada
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-" * 20)
