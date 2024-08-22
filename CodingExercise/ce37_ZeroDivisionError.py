# As you might know, it is not mathematically possible to divide a number by zero.
# Consequently, this is also not possible in Python either -you will get a ZeroDivisionError if you try:

# >>> 20 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

# With that in mind, your task for this exercise is to extend the program you created in Exercise 1
# by displaying a message to the user when they enter 0 for the "total value".

try:
    # Prompt the user to enter the total value and convert it to a float
    total_value = float(input("Enter total value: "))
    # Prompt the user to enter the value and convert it to a float
    value = float(input("Enter value: "))

    # Calculate the percentage using the formula value/total_value
    percentage = (value/total_value) * 100

    # Print the calculated percentage using f-string
    print(f"That is {percentage}%")

except ValueError:
    # Handle the case when the user doesn't enter a number
    print("You need to enter a number. Run the program again.")

except ZeroDivisionError:
    print("Your total value cannot be zero.")
