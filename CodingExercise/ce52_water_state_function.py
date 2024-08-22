"""
Define a  water_state function that:
1. gets a temperature argument
2. returns the string "Solid" if the temperature is less than or equal to 0
3. returns "Liquid" if the temperature is greater than 0, but less than 100.
4. returns "Gas" if the temperature is greater than or equal to 100.
"""


# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to 0
    if temperature <= 0:
        return "Solid"
    # Check if the temperature is between 0 and 100 (exclusive)
    elif 0 < temperature < 100:
        # Return "Liquid" if temperature is between 0 and 100
        return "Liquid"
    else:
        # Return "Gas" for all other cases
        return "Gas"


print(water_state(85))
