#Marcus McRae
#04/12/25
#P2HW2
#Grades for test

module_grades = []

module_grades.append(float(input("Enter grade for Module 1: ")))
module_grades.append(float(input("Enter grade for Module 2: ")))
module_grades.append(float(input("Enter grade for Module 3: ")))
module_grades.append(float(input("Enter grade for Module 4: ")))
module_grades.append(float(input("Enter grade for Module 5: ")))
module_grades.append(float(input("Enter grade for Module 6: ")))

lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

print("\n------------Results------------")
print(f"{'Lowest Grade:':20}{lowest}")
print(f"{'Highest Grade:':20}{highest}")
print(f"{'Sum of Grades:':20}{total}")
print(f"{'Average:':20}{average:.2f}")
print("-------------------------------")

