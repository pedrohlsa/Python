# Multiplas linhas com 3 aspas
a = """
Lorem ipsum
bla
bla
bla
"""

# Strings são arrays
a = "Hello World"
print(a[1])  # e

# Loop em string
for x in "banana":
    print(x)

# Tamanho
a = "Hello World"
print(len(a))

# Verificar presença
txt = "The best things in life are free!"
print("free" in txt)

if "best" in txt:
    print("Yes, 'best' is present.")

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Slicing
b = "Hello, World!"
print(b[2:5])   # llo
print(b[:5])    # Hello
print(b[2:])    # llo, World!
print(b[-5:-2]) # orl
