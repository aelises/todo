# Extend the given code (in the exercise area) so the code capitalizes all the names and surnames of the list
# and then prints the new list. The output of your code should be as below:

# ['John Smith, 'Jay Santi', 'Eva Kuki']

# Define the initial list of names
names = ["john smith", "jay santi", "eva kuki"]

# Use list comprehension to capitalize names and surnames
names = [name.title() for name in names]

# Print the updated list
print(names)

# The list comprehension [name.title() for name in names] is used to iterate over each name in the names list
# and apply the title() method to capitalize the first letter of each word in the name.
