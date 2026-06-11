# REPLACE() - Troca parte da string
a = "Hello, World!"
print(a.replace("H", "J"))  # Jello, World!
print(a.replace("World", "Python"))  # Hello, Python!

# SPLIT() - Divide string em lista
b = "Hello, World!"
print(a.split())  # ['Hello,', 'World!'] (corta nos espaços)

# Com separador específico
print("a,b,c".split(","))  # ['a', 'b', 'c']
print("um-dois-tres".split("-"))  # ['um', 'dois', 'tres']
