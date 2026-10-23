students = {}

for i in range(2):

    name = input("Enter name: ")

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Numbers please!")


    while True:
        try:
            grade1 = float(input("Enter your first grade: "))
            grade2 = float(input("Enter your second grade: "))
            grade3 = float(input("Enter your third grade: "))
           
            students[name] = {
                "age": age,
                "grades": [grade1, grade2, grade3]
            }
            break
           
        except ValueError:
            print("Use only numbers!")

        

print(students)

def calculate_average(grades):
    
    total = 0
    
    for item in grades:
        total += item

    total = total / len(grades)

    return total

for name in students:
    grades = students[name]["grades"]   
    average = calculate_average(grades)

    if average > 7:
        print(f"{name} | {average:.2f} | Approved")
    else:
        print(f"{name} | {average:.2f} | Failed!")