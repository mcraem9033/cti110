#Marcus McRae
#04/03/25
#P1HW2
#basic math travel expenses

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

print("\n----------- Travel Expense Summary -----------")
print(f"Location: {destination}" )
print(f"Initial Budget: {budget:.0f}")

print(f"\nFuel: {gas_expense:.0f}")
print(f"Accomodation: {accommodations_expense:.0f}")
print(f"Food: {food_expense:.0f}")

print(f"\nRemaining Balance: {remaining_budget:.0f}")




