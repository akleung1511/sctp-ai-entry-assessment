# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning


#   - Create a function called convertTemp that needs 2 pieces of information: value and unit.”
def convertTemp(value, unit):
    # If the unit is "C", convert Celsius to Fahrenheit
    if unit == "C":
        result = (value * 9/5) + 32
        # Round the result to 2 decimal places and return it
        return round(result, 2)

    # If the unit is "F", convert Fahrenheit to Celsius
    elif unit == "F":
        result = (value - 32) * 5/9
        # 
        return round(result, 2)

    # If the unit is not "C" or "F", return -1
    else:
        return -1


# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

# Add your code here
print(convertTemp(100, "C"))
print(convertTemp(32, "F"))
print(convertTemp(37, "C"))
print(convertTemp("invalid", "X"))