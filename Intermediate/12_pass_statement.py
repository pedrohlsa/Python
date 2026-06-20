# PASS STATEMENT - Placeholder "faz nada"

# Sintaxe básica
a = 33
b = 200

if b > a:
    pass  # nada acontece, só placeholder

# Por que usar pass?
# 1. Estrutura de código sem implementar lógica ainda
# 2. Onde Python exige uma declaração, mas não precisa fazer nada
# 3. Placeholder para código futuro
# 4. Funções/classes vazias

# Exemplo: função vazia
def calcular_desconto(price):
    pass  # depois implemento

# Exemplo: classe vazia
class Usuario:
    pass  # depois adiciono os métodos

# Exemplo: em condições
value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass  # ainda não decidi o que fazer com zero
else:
    print("Positive value")

#  PASS vs COMENTÁRIO
# Comentário é ignorado, mas pass é uma declaração que executa (faz nada)

# ERRADO (indentation error):
# if score > 90:
#     # isso é excelente

# CORRETO:
if score > 90:
    pass  # isso é excelente (código válido)
