#Marcus McRae
#04/23/25
#P4HW2
#Employee Time Sheet loop

'''
User will be asked to enter employee name or "Done" to terminate program 
Next user will enter pay rate and hours worked
Overtime pay and regular pay will be calculated and stored as values in variables,
At the end of the program you will display overtime total,
regular pay total, gross pay total, and number of employees entered
Prompt user to enter another employee's name to calculate salary
If no other employees are left to enter
Have user enter "Done" to terminate program
once user has no other employess to enter display totlas will populate below
'''

#Starting totals
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Initial prompt
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

while employee_name.lower() != "done":
    try:
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

        #Hours and Overtime
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            regular_hours = 40
        else:
            overtime_hours = 0
            regular_hours = hours_worked

        #Pay rate calculations
        regular_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        gross_pay = regular_pay + overtime_pay

        #Display totals
        total_employees += 1
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay

        #Display results
        print("\nEmployee name: ", employee_name)
        print("\nHours Works   Pay Rate    OverTime    OverTime Pay   RegHours Pay    Gross Pay")
        print("--------------------------------------------------------------------------------------")
        print(f"{hours_worked:<14.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}"
              f"{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

    # Prompt for next employee
    employee_name = input('\nEnter employee\'s name or "Done" to terminate: ')

# Summary output
print(f"\nTotal number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
