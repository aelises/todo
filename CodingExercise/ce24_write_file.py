# Use Python to create a file with name file.txt and write the text snail there.

file = open("../files/file.txt", "w")
file.write("snail")
file.close()

# Other Solution using with
#
# Open the file named "file.txt" in write mode using a context manager
# The 'with' statement ensures that the file is properly closed after writing

with open("../files/file.txt", "w") as file:
    file.write("snail2")     # Write the string "snail" to the file



