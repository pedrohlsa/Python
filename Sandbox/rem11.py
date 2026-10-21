def note():
    student_grades = []
    for n in range(3):
        while True:
            try:
                start = 0 
            
                grade = float(input(f"Insert your{start + 1}"))
                start += 1
                if 0 <= grade <= 10:
                    student_grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 10.")
            except ValueError:
                print("Only numbers are accepted.")
        
    return student_grades

def calculate_average(grades):
    total = 0

    for n in grades:
        total += n
    
    total = total / len(grades) 

    return total