# Create a liters_to_m3 function that:
# 1. gets a liters parameter
# 2. converts liters to cubic meters knowing that 1000 liters are equal to 1 cubic meter and returns the cubic meters.
# Note: Defining the function is enough.
# You do not need to call or print out a function output,
# but you should name the function exactly liters_to_m3.

# Define a function named liters_to_m3 that takes one parameter, liters
def liters_to_m3(liters_parameter):
    # Convert liters to cubic meters by dividing liters by 1000
    m3 = float(liters_parameter) / 1000

    # Return the result in cubic meters
    return m3


