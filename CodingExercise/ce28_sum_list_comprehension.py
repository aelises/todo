# Extend the given code so it prints out the sum of the numbers.
#
# The output of your code should be as below:

# 49.1

# Define the initial list of user entries as strings
user_entries = ['10', '19.1', '20']

# Use list comprehension to convert each item to a float
user_numbers = sum([float(item) for item in user_entries])

# Print the sum of the numbers
print(user_numbers)
