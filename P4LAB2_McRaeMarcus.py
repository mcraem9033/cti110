#Marcus McRae
#4/23/25
#P4LAB2
#Use while loop and for loop together

'''
Get integer from user
Determain if ineger is positive or negitive
if the number is positive, display multiplication table
if number is negitive, tell user program cannot accept it
ask user to run again?
if yes, run program
if no, end program
'''

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negetive values")

    run_again = input("Would you like to run again? ")

#Loop has broken. User entered 'no'
print("Program is ending...")
