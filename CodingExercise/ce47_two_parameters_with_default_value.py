"""
Define a get_age function that:
1. has two parameters, year_of_birth and current_year.
2. the current_year  parameter should be a default parameter. The default value should be the current year.
3. the function should calculate and return the age of the user given the year_of_birth and the current_year.
"""


# Define a function named get_age that takes two parameters
def get_age(year_of_birth, current_year=2024):
    # Calculate the age by subtracting the year_of_birth from the current_year
    age = current_year - year_of_birth
    # Return the calculated age
    return age


print(get_age(1968))
