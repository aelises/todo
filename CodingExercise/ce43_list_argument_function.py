# Define a function that takes a list as an argument and returns the average value of the list items.
# For example, if I called your function with foo([10, 20, 30, 40]) it should return 25,
# the average of the numbers of the list.


def foo(mylist):
    return sum(mylist) / len(mylist)


list_items = [10, 20, 30, 40]
print(f"The average is {foo(list_items)}")

