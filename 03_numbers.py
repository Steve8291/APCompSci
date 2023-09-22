print("________ Number Variables ________")
num1 = 5
num2 = 2

print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division

# Order of operations PEMDAS
subtotal = (num1 + num2) * num2
print(f"Subtotal = {subtotal}")
total = num1 + num2 * num2
print(f"Total = {total}")

# Exponents:
print(num1 ** 2)


print("\n________ Integers and Floats ________")
# Integers are whole numbers that do not have a decimal.
# Doing math with integers is faster than with decimals.
print(f"This is an int: {num1}")
# Floating Point Numbers contain a decimal place.
my_float = 5.
print(f"This is a float: {my_float}")
print(f"Division will always produce a float: {num2 / num2}")

print("\n________ Large Numbers ________")
universe_age = 14_000_000_000  # Python ignores underscores in a number.
print(f"You can use underscores to make large numbers more readable in your code: {universe_age}")

print("\n________ Multiple Assignment ________")
x, y, z = 1, 2, "my string"
print(f"You can assign multiple variables on one line. x={x}, y={y}, z={z}")

print("\n________ Constants ________")
# Constants are variables that will never change in your program.
# The convention is to capitalize constants.
PI = 3.14
SCHOOL_NAME = "Columbus East H.S."
print(f"Constants are capitalized. SCHOOL_NAME = {SCHOOL_NAME}, PI = {PI}")
