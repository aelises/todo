# The given code is incomplete. Your task is to continue that program. You need to:
# 1. calculate the percentage using the  value/total * 100 formula
# 2. print out, for example, "That is 40.0%" as shown in the sample below:
#
# The program should also print a message if the user doesn't enter a number for the "total value or for the "value":

try:
    # Prompt the user to enter the total value and convert it to a float
    total_value = float(input("Enter total value: "))
    # Prompt the user to enter the value and convert it to a float
    value = float(input("Enter value: "))

    # Calculate the percentage using the formula value/total_value
    percentage = (value/total_value) * 100

    # Print the calculated percentage using f-string
    print(f"That is {percentage}%")    # better code
    print("That is " + str(percentage) + "%")

except ValueError:
    # Handle the case when the user doesn't enter a number
    print("You need to enter a number. Run the program again.")
