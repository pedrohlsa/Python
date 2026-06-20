# DEFAULT PARAMETERS - Valor padrão para parâmetros

# Se não passar argumento, usa o valor padrão
def my_function(name="friend"):
    print("Hello", name)

my_function("Emil")      # Hello Emil
my_function("Tobias")    # Hello Tobias
my_function()            # Hello friend
my_function("Linus")     # Hello Linus

# Outro exemplo
def my_function(country="Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()            # I am from Norway
my_function("Brazil")

# Cachorro com nome padrão
def my_puppy(name="Luna"):
    print(name)

my_puppy()      # Luna
my_puppy("Rex") # Rex
