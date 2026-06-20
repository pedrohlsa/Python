# MATCH CASE - Switch case do Python (Python 3.10+)

# Sintaxe básica
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Case padrão (usando _)
day = 4

match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

# Múltiplos valores com | (OR)
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday!")
    case 6 | 7:
        print("I love weekends!")

# Guard (if extra na condição)
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April!")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May!")
    case _:
        print("No match!")
