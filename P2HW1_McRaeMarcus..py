#Marcus McRae
#04/11/25
#P2HW1
#Edit and enhance exiting programs

def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative. please try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            
print("This program calculates and displays travel expenses")

budget = get_amount("\nEnter budget: ")
destination = input("\nEnter your travel destination: ").strip()
gas_expense = get_amount("\nHow much do you think you will spend on gas? ")
accommodations_expense = get_amount("\nAprproximately, how much will you need for accommondations/hotel? ")
food_expense = get_amount("\nLast, how much do need for food? ")

             
total_expense = gas_expense + accommodations_expense + food_expense
remaining_budget = budget - total_expense

print("\n---------- Travel Expenses------------------")
print(f"{'Location:':20} {destination}" )
print(f"{'Initial Budget:':20} ${budget:.2f}")
print(f"{'Fuel:':20} ${gas_expense:.2f}")
print(f"{'Accomodation:':20} ${accommodations_expense:.2f}")
print(f"{'Food:':21}${food_expense:.2f}")
print("--------------------------------------------")
print(f"\n{'Remaining Balance:':20} ${remaining_budget:.2f}")
