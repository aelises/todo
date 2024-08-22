"""
Write a get_nr_items function that:
1. gets as a parameter one string with commas. E.g., "john,lisa, teresa"
2. the function should return the number of items divided by commas in that string
(i.e., that would be three items in the above example)
2. returns the number of items.
"""

# Define a function named get_nr_items that takes one parameter: user_input


def get_nr_items(user_input):
    # Split the user_input string by comma and store the resulting items in the 'items' list
    items = user_input.split(",")
    # Return the length of the 'items' list
    return len(items)


print(get_nr_items("john, lisa, teresa"))
