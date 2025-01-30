# ask for a user number
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")
    exit()

# initialize a list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# create a new list with all elements less than 5
b = []
for i in a:
    if i < num:
        b.append(i)

# print the new list
print("All list element less than " + str(num) + " are: " + str(b))