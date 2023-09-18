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
print(f"Division will produce a float: {num2 / num2}")
