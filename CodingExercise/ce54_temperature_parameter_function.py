"""
Define a function that:
(1) takes a temperature as a parameter
(2) returns "Hot" if the temperature is greater than 25
(3) returns "Warm" if the temperature is between 15 and 25, including 15 and 25.
(4) returns "Cold" if the temperature is less than 15.

If I called your function with foo(10) it would return "Cold".
foo(15) or foo(16) or foo(25) would all return "Warm" and foo(26) would return "Hot".
"""


def foo(temperature):
    # If the temperature is greater than 25, return "Hot"
    if temperature > 25:
        return "Hot"
    # If the temperature is between 25 and 15 (inclusive), return "Warm"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        # If the temperature is less than 15, return "Cold"
        return "Cold"


print(foo(14))
