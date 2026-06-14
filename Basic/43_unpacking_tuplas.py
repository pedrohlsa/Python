# UNPACKING - Extrair valores da tupla para variáveis

# Unpacking básico
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)   # apple
print(yellow)  # banana
print(red)     # cherry

# Com asterisco * (pega o resto)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)   # apple
print(yellow)  # banana
print(red)     # ['cherry', 'strawberry', 'raspberry'] (vira lista!)

# Asterisco no meio
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)   # apple
print(tropic)  # ['mango', 'papaya', 'pineapple']
print(red)     # cherry
