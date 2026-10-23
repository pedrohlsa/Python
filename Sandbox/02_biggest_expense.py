print("==========")
print("insert first num")
num1 = float(input())

print("==========")
print("insert second num")
num2 = float(input())

print("==========")
print("insert third num")
num3 = float(input())

if num1 <= 0 or num2 <= 0 or num3 <= 0:
    print("Please insert a number above 0")

def maiorgasto(arg1, arg2, arg3):
    if arg1 >= arg2 and arg1 >= arg3:
        maior = arg1
    elif arg2 >= arg1 and arg2 >= arg3:
        maior = arg2 
    else:
        maior = arg3

    return maior

print(f"What is the biggest number? {maiorgasto(num1, num2, num3)}")

