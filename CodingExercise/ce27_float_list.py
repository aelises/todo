# Extend the given code so the code prints out a list containing the same items as floats.
#
# The output of your code should be as below:

# [10.0, 19.1, 20.0]

# Define the initial list of user entries as strings
user_entries = ['10', '19.1', '20']

# Use list comprehension to convert each item to a float
user_codes = [float(item) for item in user_entries]

# Print the list of floats
print(user_codes)
