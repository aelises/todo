"""
Your task is to create a program that generates a random whole number. Here is how the program should behave:

Enter the lower bound: 1
Enter the upper bound: 10
7

As you can see, the program first asks the user to enter a whole number.
Then, once the user enters a number, the program asks the user again to enter another number.

Then, the program returns a random number that falls between the two whole numbers.
"""

import random

number = random.randint(1, 10)
print(number)


def random_number(lower, upper):
    whole_number = random.randint(lower, upper)
    return whole_number


# Get two numbers from the user and covert them to integers
lower_number = int(input("Enter the lower number: "))
upper_number = int(input("Enter the upper number"))

print(random_number(lower_number, upper_number))
