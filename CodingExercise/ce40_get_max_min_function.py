# The get_max function you created in the previous exercise returned 9.7.
# In this exercise, you should:
# 1. change the function so this time it returns the following string:
# "Max: 9.7, Min: 9.2"
# where 9.7 is the maximum, and 9.2 is the minimum.
# Note: For the exercise to be marked as correct by the system,
# you should return the exact string "Max: 9.7, Min: 9.2"

# Define a function named get_max
def get_max():
    # Create a list of grades
    grades = [9.6, 9.2, 9.7]
    # Find the maximum value in the grades list using the max() function
    maximum = max(grades)
    # Find the minimum value in the grades list using the min() function
    minimum = min(grades)
    # Create a message string containing the maximum and minimum values
    message = f"Max: {maximum}, Min: {minimum}"
    # Return the message string
    return message


# Call the get_max() function and print the result
print(get_max())

