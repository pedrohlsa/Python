# Precedência de Operadores (ordem de execução)

# 1. Parênteses tem a MAIOR precedência
print((6 + 3) - (6 + 3))  # 0

# 2. Multiplicação antes de adição
print(100 + 5 * 3)   # 115 (não 315)
print((100 + 5) * 3) # 315 (forçando com parênteses)

# Ordem de precedência (do maior pro menor):
# 1. ()
# 2. ** (exponenciação)
# 3. ~x, +x, -x (unários)
# 4. *, /, //, % (multiplicação/divisão)
# 5. +, - (soma/subtração)
# 6. <<, >> (bitwise shift)
# 7. & (bitwise AND)
# 8. ^ (bitwise XOR)
# 9. | (bitwise OR)
# 10. ==, !=, >, <, >=, <= (comparações)
# 11. not
# 12. and
# 13. or

# Mesma precedência: avalia da ESQUERDA para DIREITA
print(5 + 4 - 7 + 3)  # 5 (equivale a ((5+4)-7)+3)
