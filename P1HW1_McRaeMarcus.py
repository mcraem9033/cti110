# Marcus McRae
# 04/01/25
# P1LAB1
# Calculating Expoenets / Adding Subtracting

base_value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base_value ** exponent
print(f"{base_value} raised to the power of {exponent} is {result} !!")

               
starting_integer = int(input("Enter a starting integer: "))
add_number = input("Enter a number to add: ")
subtract_number = input("Enter a number to subtract: ")
add_number = int(add_number)
subtract_number = int(subtract_number)
result = starting_integer + add_number - subtract_number
print(f"{starting_integer} + {add_number} - {subtract_number} = {result}")     
