# Walrus Operator := (Python 3.8+)
# Atribui e usa na mesma expressão

# Exemplo 1: com if
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"Lista tem {count} elementos")  # Lista tem 5 elementos

# Exemplo 2: com while
while (n := input("Digite algo (ou sair): ")) != "sair":
    print(f"Você digitou: {n}")

# Exemplo 3: atribuição simples
print(x := 3)  # Printa 3 E guarda em x
print(f"x agora é {x}")
