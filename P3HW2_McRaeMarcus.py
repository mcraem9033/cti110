#Marcus McRae
#04/17/25
#P3HW2
#Employee Time Sheet

#User input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee pay rate: "))
print('-------------------------------------------')

#Hours and Overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    over_time = 0
    regular_hours = hours_worked

#Pay rate calculations
regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = regular_pay + overtime_pay

#Display results
print("Employee name: ", employee_name)
print("\nHours Works   Pay Rate    OverTime    OverTime Pay   RegHours Pay    Gross Pay")
print("--------------------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}"
      f"{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<.2f}")



    
