student = {
    "name": "Pedro",
    "age": 20,
    "grades": [8, 7, 9]
}

print(student["name"])
print(student["grades"][1])

student["grades"][1] = 15

print(student["grades"][1])

print(student["grades"][-1])

newgrade = 6

student["grades"].append(newgrade)

student["grades"].pop(1)

print(student["grades"])

student["grades"].pop(-1)

def calculate_average(student):
    total = 0
    for item in student["grades"]:
        total += item 
    return total / len(student["grades"])    

average = calculate_average(student)

if 7 <= average <= 10:
    print(f"Approved! {average:.2f}")

elif 5 <= average < 7:
    print(f"Recovery! {average:.2f}")

else:
    print(f"Failed! {average:.2f}")


''