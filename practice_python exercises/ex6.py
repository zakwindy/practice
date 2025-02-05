# ask the user for a string
user_str = str(input("Enter a string: "))

# check if the string is a palindrome
if user_str == user_str[::-1]:
    print(user_str, "is a palindrome.")
else:
    print(user_str, "is not a palindrome.")