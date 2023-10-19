#!/usr/bin/env python3

# sudo pip3 install colorama

import random
import time
from colorama import Fore
from colorama import Style


difficulty_level = 20  # The lower the number the harder the game. Default 1:20 chance of monster.
directions = ["n", "north", "s", "south", "e", "east", "w", "west"]
options_list = ["help", "take axe", "throw axe", "take treasure"]
all_options = directions + options_list
available_object = ""
monsters = []
satchel = []
moves = 0
available_monsters = [
    "Bake-danuki a mischievous monster raccoon dog",
    "Kitsune a magical shape shifting fox",
    "Kappa a water god with features resembling an amphibian and human",
    "Tengu a mysterious red-faced monster with a very long nose",
    "Shikigami a dark and terrifying monster with magical powers",
    "Tsukumogami an evil umbrella that has been inhabited by a kami spirit"
]


def output_text(text):
    print(f'\n{Fore.GREEN}{text}{Style.Reset_ALL}', end='')


def gunma_prefecture():
    message = """
    The sun is quickly going down in the west as you look around Gunma Prefecture.
    The great mountain of Akagi lies ahead to the north. Dark alleyways lead in the other directions.
    Which direction would you like to travel?
    """

    print(message)
    user_input = ""
    while user_input not in directions:
        check_monster()
        user_input = input(">").lower()
        # Better method
        # if user_input in ("n", "north"):
        if user_input == "n" or user_input == "north":
            miyagi_village()
        elif user_input == "s" or user_input == "south":
            dark_alley()
        elif user_input == "e" or user_input == "east":
            dark_alley()
        elif user_input == "w" or user_input == "west":
            yasaka_shrine()
        else:
            other_options(user_input)





###### Add new functions here to create new rooms. #######




def game_over():
    global moves
    global available_object
    global available_monsters
    moves = 0
    available_object = ""
    monsters.clear()
    satchel.clear()
    available_monsters = [
        "Bake-danuki a mischievous monster raccoon dog",
        "Kitsune a magical shape shifting fox",
        "Kappa a water god with features resembling an amphibian and human",
        "Tengu a mysterious red-faced monster with a very long nose",
        "Shikigami a dark and terrifying monster with magical powers",
        "Tsukumogami an evil umbrella that has been inhabited by a kami spirit"
    ]

    print("Type \"start\" to begin a new game or enter any other key to end.")
    user_input = input(">").lower()
    if user_input == "start":
        print(f"Good luck {name}. You are probably going to need it!\n")
        time.sleep(4)
        gunma_prefecture()
    else:
        exit()


def win():
    banner = """
    :::   :::  ::::::::  :::    :::      :::       ::: ::::::::::: ::::    :::      :::
    :+:   :+: :+:    :+: :+:    :+:      :+:       :+:     :+:     :+:+:   :+:      :+:
     +:+ +:+  +:+    +:+ +:+    +:+      +:+       +:+     +:+     :+:+:+  +:+      +:+
      +#++:   +#+    +:+ +#+    +:+      +#+  +:+  +#+     +#+     +#+ +:+ +#+      +#+
       +#+    +#+    +#+ +#+    +#+      +#+ +#+#+ +#+     +#+     +#+  +#+#+#      +#+
       #+#    #+#    #+# #+#    #+#       #+#+# #+#+#      #+#     #+#   #+#+#
       ###     ########   ########         ###   ###   ########### ###    ####      ###
    """
    print(banner)
    exit()


def other_options(user_input):
    global available_object
    if user_input not in options_list:
        print("I don't know how to do that.\n")
    elif user_input == "help":
        print("\nHere is a list of possible commands:")
        for option in all_options:
            print(f"  {option}")
    elif user_input == "take treasure":
        if available_object == "treasure":
            print("    You have picked up the treasure!\n\n")
            time.sleep(1)
            win()
        else:
            print("    There is no treasure here to pick up. Who do you think you are fooling?")
            check_monster()
    elif user_input == "take axe":
        if available_object == "axe":
            print("    You have picked up an axe.")
            satchel.append("axe")
            available_object = ""
        else:
            print("    There is no axe here to pick up.")
    elif user_input == "throw axe":
        if "axe" in satchel:
            if monsters:
                monster = monsters.pop(0)
                print(f"    You throw your axe at the {monster} and cleave its head clear off.")
                print(f"    You see your axe lying in a pool of blood beside the slaughtered {monster}.")
            else:
                print("    I don't know why you would throw away a good axe.")
                print("    You see your axe lying on the ground in front of you.")
            available_object = "axe"

        else:
            print("    You have no axe to throw.")


def check_monster():
    global moves
    if moves >= 5:
        print(f"    The {monsters[0]} has consumed your soul. You have died!")
        game_over()
    monster_roll = random.randint(1, difficulty_level)
    if monster_roll == 1 and available_monsters:
        new_monster = available_monsters.pop(random.randrange(len(available_monsters)))
        monsters.append(new_monster)
        print(f"The {monsters[-1]} appears and looks like it wants to eat you!")
    if monsters:
        for monster in range(len(monsters)):
            print(f"    You are being chased by the {monsters[monster]}!")
        print("    They are gaining on you. Better move quick.")
        moves += 1
    else:
        moves = 0


while True:
    print("""
        ##############################################
        ##############################################
        Welcome to the Greatest Adventure of All Time!
        ##############################################
        ##############################################
        """)
    name = input("Please enter your name: ")

    message = """

    As an intrepid treasure hunter, you have decided to go on a quest to find Tokugawa's buried treasure.
    Your quest has taken you across oceans and into the distant land of Japan.
    You find yourself in Gunma Prefecture at the base of the massive stratovolcano known as Mount Akagi.
    If the legends are true then somewhere on or in this moutain lies hidden a great treasure.
    You can choose to walk in multiple directions to find your way by typing (n)orth, (s)outh, (e)ast, (w)est.
    If you ever need help you can simply type "help" to see a list of possible commands.

    """

    output_text(message)
    print(f"Good luck {name}. You are probably going to need it!\n")
    time.sleep(4)
    gunma_prefecture()