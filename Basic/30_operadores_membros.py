# Operadores de Associação (Membership): in / not in
# Verificam se um valor existe em uma sequência

# Com listas
fruits = ["apple", "banana", "cherry"]
print(f"banana in fruits: {'banana' in fruits}")        # True
print(f"pineapple not in fruits: {'pineapple' not in fruits}")  # True

# Com strings (case sensitive!)
text = "Hello World!"
print(f"'H' in text: {'H' in text}")        # True
print(f"'h' in text: {'h' in text}")        # False (case sensitive)
print(f"'Hello' in text: {'Hello' in text}") # True
print(f"'z' not in text: {'z' not in text}") # True

# Com números
nums = [1, 2, 3, 4, 5]
print(f"3 in nums: {3 in nums}")    # True
print(f"10 in nums: {10 in nums}")  # False
