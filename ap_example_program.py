#!/usr/bin/python3


name_list = [
    'bob brown',
    'susan williams',
    'sally martinez',
    'alice gonzalez',
    'beatrice miller',
    'daisy wilson',
    'silas anderson',
    'bob thomas',
    'alice lopez',
    'bob taylor'
]


def isEqual(value1, value2):
    if value1 == value2:
        return True
    else:
        return False


def name_count(name):
    count = 0
    name = name.lower()
    name = name.strip()
    for i in name_list:
        i = i.split(' ', 1)[0]
        if isEqual(i, name):
            count += 1
    return count


def hello(first_name, last_name):
    print(f"Hello {first_name.title()} {last_name.title()}")


def known_name(first_name, last_name):
    full_name = first_name.lower() + " " + last_name.lower()
    print(full_name)
    if full_name in name_list:
        return True
    else:
        name_list.append(full_name)


# Main Program
while True:
    user_input = input("\nPlease enter a first and last name or 'quit' to end: ")
    if user_input == 'quit':
        print("\nGoodby!\n")
        quit()

    split_name = user_input.split()
    if len(split_name) != 2:
        user_input = ''
    else:
        first_name, last_name = split_name[0], split_name[1]
        first_count = name_count(first_name)
        hello(first_name, last_name)
        print(f'Your first name "{first_name.title()}" appears in list {first_count} times!')
        if known_name(first_name, last_name):
            print("We know who you are and are watching you...")
        else:
            print("We do not know who you are. However, we are now tracking you...")
