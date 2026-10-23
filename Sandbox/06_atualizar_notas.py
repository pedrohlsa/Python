student = {}
grades = []

name = input("Enter student name: ")
age = int(input("Enter age: "))
qty = int(input("How many grades do you want to add?")) 

for n in range(qty):
    while True:
        
        grade = float(input(f"Enter grade: #{n + 1}"))

        if 0 <= grade <= 10:
            grades.append(grade)
            break
        else:
            print("Only allowed notes between 0 and 10.")

student["name"] = name
student["age"] = age
student["grade"] = grades 
    
try:
    print("Want to correct/update any grade ? ")
    print("1. Y | 2. N")
    option = int(input())
except ValueError:
    print("Only nums are accept!")
    option = 0

def showlist(grade,name):
    for item in grade, name:
        print(f"{name} {grade}")


if option == 1:
    
    print("What note do you want to update/correct? ")
    opt = int(input("1. First Note | 2. Second Note | 3. Third Note | 4. All Notes"))

    while True:
        if opt == 1:
            updategrade = float(input(f"Insert your #{opt} note "))
            if 0 <= updategrade <= 10:
                print("Allowed.")
                student["grade"][0] = updategrade
                break
            else:
                print("Only notes between 0 and 10 are accept.")
        
        elif opt == 2:
            updategrade = float(input(f"Insert your note #{opt}"))
            if 0 <= updategrade <= 10:
                print("Allowed.")
                student["grade"][1] = updategrade
                break
            else:
                print("Only nums between 0 and 10 are accept.")
        elif opt == 3:
            updategrade = float(input(f"Insert your note #{opt}"))
            if 0 <= updategrade <= 10:
                print("Allowed.")
                student["grade"][2] = updategrade
                break
            else:
                print("Only nums between 0 and 10 are accept.")
        
        else:
            student["grade"].clear()
            qty2 = int(input("How many notes do you want to add? "))

            for n in range(qty2):
                while True:

                    grade2 = float(input(f"Insert your #{n + 1} note"))

                    if 0 <= grade2 <= 10:
                        grades.append(grade2)
                        break
                    else:
                        print("Only allowed notes between 0 and 10.")
            break
