import random

print("________ Lists ________")
# To create a list you use square brackets: []
skateboards = ['Santa Cruz', 'Powell Peralta', 'Girl', 'Anti-Hero']
print(skateboards)

print("\n________ Accessing List Elements ________")
# Lists are zero indexed so the first element is number 0.
print(skateboards[0])
print(skateboards[2])
print(skateboards[1].lower())  # String formatting works on lists too.

# To access the last item in a list you can use [-1]
print(skateboards[-1])
# You can also reference list items from the end of the list.
print(skateboards[-3])  # To count from the end of the list, start at -1
print(f"My fist skateboard was a {skateboards[0]} - Rob Roskopp.")  # You can use values from a list anywhere.

# Practice: Make your own list of items and print each one on a separate line.

print("\n________ Changing Elemets in a List ________")
skateboards[0] = 'Element'
print(skateboards)

print("\n________ Appending Elements to the End of a List ________")
skateboards.append('Enjoi')
print(skateboards)
snowboards = []  # Empty list
snowboards.append('K2')
snowboards.append('Burton')
snowboards.append('Arbor')
print(snowboards)

print("\n________ Inserting Elements into a List ________")
snowboards.insert(0, 'Avalanche')  # Create a new space at beginning of list and inserts.
print(snowboards)
snowboards.insert(2, 'Sims')
print(snowboards)

print("\n________ Removing Elements from a List ________")
del snowboards[0]
print(snowboards)

# The pop() method lets you remove the last item in a list.
# It also allows you to store and use that item.
old_board = snowboards.pop()
print(f"Once upon a time I owned an {old_board} snowboard.")
print(snowboards)

# Using pop() to remove a specific item:
favorite_board = snowboards.pop(1)
print(f"One of my favorite boards was a {favorite_board}")
print(snowboards)

# Moving an element from one list to another:
movies = ['Meaning of Life', 'Life of Brian', 'The Holy Grail']
print(movies)
watched_movies = []
watched_movies.append(movies.pop(1))
print(movies)
print(watched_movies)

print("\n________ Removing Item by Value ________")
# If you know the value of the item but not its location in the list.
awesome_cars = ['Supra', 'Trans Am', 'VW Beetle', 'Aston Martin']
print(awesome_cars)
awesome_cars.remove('VW Beetle')
print(awesome_cars)

# print("\n________ Sorting a List Permanently with the sort() Method ________")

print("\n________ Select Random Item From List ________")
fruits = ["apple", "banana", "cherry", "peach", "pear"]
random_fruit_1 = random.choice(fruits)
print(random_fruit_1)
random_fruit_2 = random.choice(fruits)
print(random_fruit_2)

print("\n________ Get Length of a List ________")
size = len(fruits)
print(size)
print(fruits)
