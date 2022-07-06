# user interactions

import database

MENU_PROMPT = """
Please choose

1) Add a coffee bean
2) See all coffee beans
3) Find a coffee bean by name
4) See how best to prepare a particular bean
5) Exit.

Your selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            print("you selected 1")
        elif user_input == "2":
            print("you selected 2")
        elif user_input == "3":
            print("you selected 3")
        elif user_input == "4":
            print("you selected 4")
        else:
            print("Invalid input, please try again")


menu()
