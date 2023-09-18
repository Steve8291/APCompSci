# Examples of using variables
# Variable names can only contain letters, numbers, and underscores.
# Can not start with a number.
# Variable names should be short but descriptive:
d = "Fido"  # Not a good name
dog = "Fido"  # Good name
# Use underscores for longer names:
new_dog = "Spot"


print("________ String Variables ________")
message = "This is a string. It must be in single or double quotes."
print(message)
print("message")  # Will not print your variable.

# The type() function will return the variable type:
print(type(message))

# You can change the value of a variable at any time:
message = "Here is a new message"
print(message)

# Error Messages:
#   print(mesage)

# Using quotes in a string:
print('Single quotes allow me to use "double quotes" in a string!')
print("Or with double quotes I could use 'single quotes'!")
print("Another way is to escape the quote with a \"backslash\" like this.")
print("Backslashes can also be used to create a newline\nThis is on the next line.")
print("You can also add in tabs.\tThis is tabbed over once.\t\tTwo tabs here")

print("\n_________ String Methods ________")
name = "peter pantz"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "max"
middle_init = "E"
last_name = "mumm"

# fstrings
full_name = f"{first_name} {last_name}"
print(full_name)
# Add the middle name:
full_name = f"{first_name} {middle_init} {last_name}"
print(full_name)
# Capitalize words:
print(full_name.title())
# Add a period:
full_name = f"{first_name} {middle_init}. {last_name}"
print(full_name.title())

# Create a sentence using both of the names:
print(f"{full_name.title()} gave his spare clothes to {name.title()}!!")
# Note: It would be cleaner to save the variables with the string formatting before using them.
name = name.title()

# Stripping whitespace:
best_friend = ' Bilbo Baggins    '
message = 'says "not all those who wander are lost.."'
print(best_friend)
print(best_friend.rstrip(), message)  # Right Strip
print(best_friend.lstrip(), message)  # Left Strip
print(best_friend.strip(), message)  # Strip all whitespace

# Wrapping really long lines of code to make them easier to read:
# Use a backslash to ignore the newlines.
sir_robin = "\nBrave Sir Robin ran away. \
Bravely ran away away. \
When danger reared it’s ugly head, he bravely turned his tail and fled. \
Brave Sir Robin turned about and gallantly he chickened out…"
print(sir_robin)  # This should print on one line.


# Multiline Strings or heredocs:
text = """
This is a multiline string.
My favorite languages are:
\tPython
\tBash
\tC++
\tPerl
"""

print(text)


# Variables in a heredoc using fstrings:
# Notice a backslash can be used to ignore the first empty line.
lang = "lua"
text = f"""\
This is a multiline fstring.
My favorite languages are:
\tPython
\tBash
\tC++
\t{lang}
    Perl
"""

print(text)
