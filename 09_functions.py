#!/usr/bin/env python3

# Functions are a way to write cleaner and more reusable code.
# Use a function whenever your program will have to repeat a task.
# They will make your code easier to write, read, test, and fix.
# Think of them like programs within a program.

def greet_user():
    """Display a simple greeting"""
    print("Hello!")


greet_user()


# Passing information to a function.
def say_hello(user_name):
    """Takes a single name as an argument and says hello."""
    print(f"Hello, {user_name.title()}!")


# Technically, "bobby bubbles" is an argument and 'user_name' is a parameter
say_hello("bobby bubbles")

# Try writing your own function that takes a parameter and prints a message.


def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Call function with Positional Arguments
print("\n________ Positional Parameters ________")
describe_pet("cat", "max")

# Call function with Keyword Arguments
print("\n________ Keyword Arguments ________")
describe_pet(animal_type='hamster', pet_name='harry')
# Order does not matter!
describe_pet(pet_name='shadowfax', animal_type='horse')


def describe_car(model, manufacturer, speed=100):
    """Display information about a car"""
    print(f"I have a {manufacturer.title()} {model.title()}.")
    print(f"My {model.title()} goes {speed} mph!")


print("\n________ Default Values ________")
describe_car('Prius', 'Toyota')
describe_car('Bug', 'VW', 60)  # Note that we passed an int here.

# When using default values always put them at the end of the parameter list.
# Otherwise Python will interpret them by position.
# def bad_position(animal='dog', name):
#     """Incorrect way to add default values!!!!"""
#     print(f"I have a {animal}.")
#     print(f"My {animal}'s name is {name.title()}.")

# bad_position('fido')

# Try writing a function called `describe_city()` that accepts the name of a city and its country.
# Give one of these parameters a default value.
# The function should print a message using these parameters.


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


print("\n________ Return Values ________")
musician = get_formatted_name('katy', 'perry')
print(musician)


def get_full_name(first_name, last_name, middle_name=''):
    """Return a full name with optional middle name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


print("\n________ Optional Arguments ________")
musician = get_full_name('jimmy', 'hendrix')
print(musician)
musician = get_full_name("Sir James", "McCartney", "Paul")
print(musician)

