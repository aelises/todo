# Write a program that reads the essay.txt file and returns the number of characters contained in the file.

file = open("../files/essay.txt", "r")
characters = file.read()
print(len(characters))
