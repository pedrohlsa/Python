# Função que retorna booleano
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

# Verificando variáveis
x = "Hello"
y = 15

print(bool(x))  # True
print(bool(y))  # True

# Exemplo prático: verificar se lista está vazia
lista = []
if bool(lista):
    print("Lista tem itens")
else:
    print("Lista está vazia")  # Vai imprimir isso

# Com __len__ (método especial)
class myclass():
    def __len__(self):
        return 0  # Se for 0, bool retorna False

myobj = myclass()
print(bool(myobj))  # False
