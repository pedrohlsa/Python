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

def showlist(grade,name):
    for item in grade, name:
        print(f"{name} {grade}")


if option == 1:
    
    print("What note do you want to update/correct? ")
    opt = int(input("1. First Note | 2. Second Note | 3. Third Note | 4. All Notes"))

    while True:
        if opt == 1:
            grade[0] = float(input("Enter your note: "))
            if grade[0] <= and <= 10:
                print("Allowed.")
                break
            else:
                print("Only nums between 0 and 10 are accept.")
        
        elif opt == 2:
            grade[1] = float(input("Enter your note: "))
                    if grade[0] <= 0 and <= 10:
                        print("Allowed.")
                        break
                    else:
                        print("Only nums between 0 and 10 are accept.")
        elif opt == 3:
            grade[1] = float(input("Enter your note: "))
                    if grade[0] <= 0 and <= 10:
                        print("Allowed.")
                        break
                    else:
                        print("Only nums between 0 and 10 are accept.")
        else:
            student.pop("grade")

