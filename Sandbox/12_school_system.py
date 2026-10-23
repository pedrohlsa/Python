print("======== SCHOOL SYSTEM ==========")

students = {}

def calculate_average(grades):
    total = 0

    for item in grades:
        total += item

    total = total / len(grades)

    return total

while True:
    print("Welcome!")


    try: 
        op = int(input("1. | Register student | 2. Show all Students | 3. Search Student By ID | 4. Exit"))

        if op == 4:
            break

        elif op == 1:
            
            while True:
                try:
                    op2 = int(input("How many students want to add? "))
                    for i in range(op2):

                        while True:
                            try:
                                studentID = int(input("Student ID: "))
                                
                                if studentID not in students:
                                     break
                                else:
                                    print("Student already registered.")
                            
                            except ValueError:
                                print("Only numbers are accepted!")
                        
                        name = input("Name: ") 

                        while True:
                            try:
                                age = int(input("Age: "))
                                break
                            except ValueError:
                                print("Only intengers and numbers are accept.")
                            
                        grades = []

                        while True:
                            try:
                                op3 = int(input("How many grades do you want to add?"))

                                if op3 <= 0:
                                    print("Please, insert at least 1 note to inserte!")
                                else:
                                    for i in range(op3):
                                        while True:
                                            
                                            try:
                                                grade = float(input(f"insert your {i + 1} note: "))        
                                            
                                                if 0 <= grade <= 10:
                                                    grades.append(grade)
                                                    break
                                                else:
                                                    print("Please, use nums between 0 and 10")
                                            except ValueError:
                                                print("Only nums please!")
                                    break
                            except ValueError: 
                                print("Only numbers are accepted!")

                        students[studentID] = {
                            "name": name,
                            "age": age,
                            "grades": grades  
                        }

                    break
                except ValueError:
                    print("Only numbers are accepted!")            

        elif op == 2:
            
            while True:
                try:
                    op4 = int(input("1. Show all students | 2. Show if Failed or Pass"))
                    
                    if op4 == 1:   
                        for identification, info in students.items():
                            print(f"ID: {identification} | Name: {info['name']} | Age: {info['age']} | Grades: {info['grades']}")
                        break

                    elif op4 == 2:

                        for identification, info in students.items():
                            
                            average = calculate_average(info['grades'])
                            status = "Pass" if average >= 7 else "Failed"
                            
                            print(f"ID: {identification} | Name: {info['name']} | Note: {average:.2f} | Status: {status}")
                        
                        break
                
                except ValueError:
                    print("Only numbers are accepted!")
        elif op == 3:

            print("Search page!")

            try:
                op5 = int(input("Enter your Student ID: "))
                
                if op5 in students:
                    print(f"{students[op5]}")
                else:
                    print("Student not Found")
            
            except ValueError:
                print("Only numbers are accepted!")

        else:
            print("Please, use nums between 1-4.")
    
    except ValueError:
        print("Only numbers are accepted!")  
    