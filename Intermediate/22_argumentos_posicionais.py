# ARGUMENTOS POSICIONAIS - Ordem importa

# Função espera 2 argumentos NA ORDEM
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")  # Emil Refsnes

# ERRADO: número de argumentos diferente
# my_function("Emil")  # TypeError: missing 1 required positional argument

# Exemplo prático
def criar_usuario(nome, idade, cidade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

criar_usuario("João", 25, "SP")
