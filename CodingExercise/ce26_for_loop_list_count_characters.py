# Extend the given code so the code prints out a list containing the number of characters for each username.
#
# The output of your code should be as below:
# [9, 11, 11]

# Define the initial list of usernames
usernames = ["john 1990", "alberta1970", "magnola2000", "paddy"]

# Use list comprehension to calculate the number of characters for each username
characters = [len(username) for username in usernames]

# Print the list of character counts
print(characters)
