# Conditionals

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

print("________ If Statement ________")
a = 33
b = 200
if b > a:
    print("b is greater than a")


print("\n________ Else If Statement ________")
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


print("\n________ Else Statement ________")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


print("\n________ And Statement ________")
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")


print("\n________ Or Statement ________")
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


print("\n________ Not Statement ________")
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")


print("\n________ Nested If Statement ________")
# Indentation matters. Notice how the `else` statement is part of the nested `if`
# See if you can add an `else` to the first `if x> 10:` statement
# Test this with different values for x
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("Not above 10")


print("\n________ Test Variable Type ________")
my_string = "This is a string"
my_int = 8
my_float = 8.8
print(type(my_float))

variable = my_string
if isinstance(variable, int):
    print("The variable actually was an int")
else:
    print(f"The variable was not an int, it was a: {type(variable)}")
