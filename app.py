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
            name = input("Enter Coffee Bean name: \n").title()
            method = input("Enter how you prepared your coffee: \n").title()
            rating = int(input("How do you score the coffee out of 100?: \n"))

            if rating >100 or rating < 0:
                rating = int(input("Invalid score, please rate 0-100: \n"))

            database.add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = database.get_all_beans(connection)
            # For loop prints each row as a new line (print(beans) prints them in a list)
            for bean in beans:
                print(bean)
        elif user_input == "3":
            print("you selected 3")
        elif user_input == "4":
            print("you selected 4")
        else:
            print("Invalid input, please try again")


menu()
