print("________ Dictionaries ________")
# To create a dict you use curly brackets: {}
# Dicts have keys and values: "key": "value" pairs
# You can store any data type in a Python dict.
# Dicts can not have duplicate keys.
# Dicts are both ordered and changeable.
car_dict = {
    "brand": "Ford",
    "model": "Mustang",  # String
    "liters": 5.0,       # float
    "sweet_ride": False,  # bool
    "year": 1964,        # int
    # "year": 1999
}
print(car_dict)


print("\n________ Access the Value of a Key ________")
# nameOfDict["key"]
print(car_dict["brand"])


print("\n________ Dictionary Length ________")
print(len(car_dict))


print("\n________ Change Item in Dict ________")
car_dict["sweet_ride"] = True
print(car_dict)


print("\n________ Add New Item to Dict ________")
car_dict["color"] = "Red"
print(car_dict)


print("\n________ Check if Key Exists ________")
# Check if "liters" exists as a key in the dict
if "liters" in car_dict:
    print("Yes, 'liters' is one of the keys in this dictionary.")
    liters = car_dict["liters"]  # Storing a dictionary item in a new variable
    print(f"This {car_dict['brand']} {car_dict['model']} is {liters} Liters!")


print("\n________ Delete Item From Dict ________")
if "year" in car_dict:
    del car_dict['year']
print(car_dict)


print("\n________ Nested Dictionaries ________")
# These are dictionaries that contain dictionaries!
academic_schools = {
    "Indiana University": {
        "cost": 20000,
        "location": "Bloomington, Indiana",
        "degrees": ("Computer Science", "Business", "Geology"),
        "gpa": 3.0,
        "sat_score": 1000
    },
    "MIT": {
        "cost": 50000,
        "location": "Cambridge, MA",
        "degrees": ("Computer Science", "Botany", "Paleontology"),
        "gpa": 4.0,
        "sat_score": 1500
    }
}

print("\n__Print MIT gpa:")
print(academic_schools["MIT"]["gpa"])

print("\n__Print degrees list from MIT:")
for i in academic_schools["MIT"]["degrees"]:
    print(i)

print("\n__Print List of Keys:")
for i in academic_schools.keys():
    print(i)
