# LOOP EM LISTAS - 3 formas diferentes

thislist = ["apple", "banana", "cherry"]

# 1. For loop direto (mais comum)
print("--- For direto ---")
for x in thislist:
    print(x)

# 2. For com range e len (usando índice)
print("--- For com índice ---")
for i in range(len(thislist)):
    print(thislist[i])

# 3. While loop
print("--- While loop ---")
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# 4. List comprehension (mais curto)
print("--- List comprehension ---")
[print(x) for x in thislist]
