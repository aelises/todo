# Please code this exercise in your computer IDE.
# For this exercise, download the members.txt file attached to the resources.
# Then, create a program that:
#
# 1. prompts the user to enter a new member.
# 2. adds that member to members.txt at the end of the existing members.
# For example, the user here has entered the member Solomon Right.

while True:
    input_member = input("Enter a new member: ") + "\n"
    file = open("../files/members.txt", "r")
    member = file.readlines()
    file.close()

    member.append(input_member)
    file = open("../files/members.txt", "w")
    file.writelines(member)
    file.close()
