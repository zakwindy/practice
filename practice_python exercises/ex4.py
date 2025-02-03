# ask the user for a number
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")
    exit()

# initialize a list of numbers up to the given number
list = range(1, num + 1)

# create a new list of divisors of the given number
divisors = []
for i in list:
    if num % i == 0:
        divisors.append(i)

# print the new list
print("All divisors of " + str(num) + " are: " + str(divisors))