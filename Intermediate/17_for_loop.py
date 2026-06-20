# FOR LOOP - Itera sobre sequências

# Lista
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# String (cada caractere)
for x in "banana":
    print(x)

# Break no for
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Break antes do print (não printa banana)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)  # apple

# else no for
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# for com else e break (else NÃO executa se break acontecer)
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished")  # Não executa por causa do break
