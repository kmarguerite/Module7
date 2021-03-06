#!usr/bin/env Python 3

"""
This script will create a dictionary of names and usernames.

Goals: use github to push changes

To run this script from the command line type:
python hw7.py

Assumptions:

Requires:
Anaconda Python3
"""

from sortedcontainers import SortedDict

#menu of options
def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Username')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'
usernames['Kate'] = 'HedgehogBestie'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    while True:
        try:
            menu_choice = int(input("Type in a number (1-5): "))
            break
        except ValueError:
            print("That was not a number, please select a number!")

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        if name in usernames:
            usernames.pop(name)
        else:
            print ("Name not found!")

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print("Username found! Their username is: {}".format(usernames[name]))
        else:
            print ("username not found!")

    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print("Sorry! {} is not a menu option! Please make another selection".format(menu_choice))
        print_menu()

