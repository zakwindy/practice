import random

# define two random lists
len_a = random.randint(1, 20)
len_b = random.randint(1, 20)

a = random.sample(range(1, 100), len_a)
b = random.sample(range(1, 100), len_b)

# create a new list that contains only the elements that are common between the lists
c = [i for i in a if i in b]
print("List a: ", a)
print("List b: ", b)
print("Common elements: ", c)