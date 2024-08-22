# We have a list of two IPs in the code area.
# Extend the code so your program:
# 1. Prompts the user to input an index (e.g., 0 or 1).
# 2. Depending on the user input, the program should return either You chose 100.122.133.111
# or You chose 100.122.133.111
# Note: In order for the system to mark your exercise as correct,
# your code should return the exact output (i.e., upper case Y in You chose and no spaces
# or other characters after the IP.

ips = ['100.122.133.105', '100.122.133.111']

# Prompt the user to input the index of the IP they want and convert it to an integer.
user_choice = int(input("Enter the index of the IP you want: "))

# Create a formatted message string that includes the chosen IP based on the user's input.
message = f"You chose {ips[user_choice]}"

# Print the message.
print(message)


