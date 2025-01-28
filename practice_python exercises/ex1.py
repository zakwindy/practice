#ask the user for name and age
name = input("What is your name? ")

try:
    age = int(input("What is your age? "))
    times = int(input("How many times do you want to see the message? "))
except ValueError:
    print("Please enter a valid number")
    exit()

#calculate the year when the user will turn 100
year = 2025 + (100 - age)

#print the year
output = name + ", you will turn 100 in the year " + str(year) + "\n"
print(times * output)