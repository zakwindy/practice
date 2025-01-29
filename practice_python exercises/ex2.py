# ask the user for a number
try:
    num = int(input("Enter a number: "))
    check = int(input("Enter a number to check if the first number is divisible by it: "))
except ValueError:
    print("Please enter a valid number")
    exit()

#check if the number is divisible by 4, 2 or neither
if num % 4 == 0:
    print("The number is divisible by 4")
elif num % 2 == 0:
    print("The number is even but not divisible by 4")
else:
    print("The number is odd")

#check if the number is divisible by the check number
if num % check == 0:
    print("The number is divisible by " + str(check))
else:
    print("The number is not divisible by " + str(check))