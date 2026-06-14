# LOOP em tuplas (igual listas)

thistuple = ("apple", "banana", "cherry")

# 1. For direto
print("--- For direto ---")
for x in thistuple:
    print(x)

# 2. For com range e len
print("--- For com índice ---")
for i in range(len(thistuple)):
    print(thistuple[i])

# 3. While loop
print("--- While loop ---")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Juntar tuplas (operador +)
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # ('a', 'b', 'c', 1, 2, 3)
