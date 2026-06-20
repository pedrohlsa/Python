# ARGUMENTOS KEYWORD (nomeados) - Ordem NÃO importa

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

# Keyword arguments (ordem não importa)
my_function(animal="dog", name="Buddy")
my_function(name="Buddy", animal="dog")  # mesma coisa

# Exemplo com kwargs (Keyword Arguments)
def my_function(fname, lname):
    print(fname + " " + lname)

my_function(fname="Emil", lname="Refsnes")

# Misturando posicional com keyword
def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, c=3)    # ✅
my_function(1, b=2, c=3)  # ✅
# my_function(a=1, 2, 3)  # ❌ (keyword não pode vir antes de posicional)
