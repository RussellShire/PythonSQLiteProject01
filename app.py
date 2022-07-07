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
    database.create_tables(connection, database.CREATE_BEANS_TABLE)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            prompt1_add_bean(connection)
        elif user_input == "2":
            prompt2_get_beans(connection)
        elif user_input == "3":
            prompt3_get_by_bean(connection)
        elif user_input == "4":
            prompt4_best_preparation(connection)
        else:
            print("Invalid input, please try again")


def prompt1_add_bean(connection):
    name = input("Enter Coffee Bean name: \n").lower()
    method = input("Enter how you prepared your coffee: \n").lower()
    rating = int(input("How do you score the coffee out of 100?: \n"))

    if rating > 100 or rating < 0:
        rating = int(input("Invalid score, please rate 0-100: \n"))

    database.add_bean(connection, name, method, rating)


def prompt2_get_beans(connection):
    beans = database.get_all_beans(connection)
    # For loop prints each row as a new line (print(beans) prints them in a list)
    for bean in beans:
        print(f"{bean[1].title()} ({bean[2].title()}) - {bean[3]}/100")


def prompt3_get_by_bean(connection):
    name = input("Enter coffee bean name:\n").lower()

    beans = database.get_beans_by_name(connection, name)
    for bean in beans:
        print(f"{bean[1].title()} ({bean[2].title()}) - {bean[3]}/100")


def prompt4_best_preparation(connection):
    name = input("What coffee do you want to know the best preparation for?:\n")

    best_method = database.get_best_method(connection, name)

    print(f"The best preparation method for {name.title()} is: {best_method[2].title()}")


menu()
