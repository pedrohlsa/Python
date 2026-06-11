x = "awesome"

def myfunc():
    print("Python is " + x)  # usa global

myfunc()

def anotherfunc():
    x = "Fantastic"  # local
    print("Python is", x)

anotherfunc()
print("Python is", x)  # ainda "awesome"

# Tornar local em global
def globalfunc():
    global x
    x = "fantastic"

globalfunc()
print("Python is", x)  # agora "fantastic"
