import numpy as np  # are we using this
import pandas as pd
import os  # and this


def add_books(booklist):
    books = []
    while True:
        book_name = input("Enter name of book: ")
        borrowed = input("Has it been borrowed?: ")
        price = input("Price of item: ")

        while borrowed.lower() not in ["yes", "no", "y", "n"]:
            borrowed = input("Has it been borrowed? (yes/no): ")

        if borrowed.lower() in ["y", "yes"]:
            borrowed = True
        else:
            borrowed = False

        books.append([book_name, borrowed, price])

        cont = input("Add another book?: ")

        if cont.lower() in ["no", "n"]:
            break

    new_book = pd.DataFrame(books, columns=["Book", "Borrowed", "Price"])
    booklist = booklist.append(new_book, sort=False)
    booklist.to_csv(DIVERTED_PATH, index=False)


def getList(booklist):
    pd.set_option('display.max_rows', 1000)
    print(booklist)


def availability(booklist):
    available = booklist.loc[booklist["Borrowed"] == False, ["Book", "Price"]]
    print("Available books:")
    print(available)


def main(path):
    menu = ("----------------------------------------\n"
            "Main Menu\n"
            "----------------------------------------\n"
            "[0] Add Books\n"
            "[1] Get Booklist\n"
            "[2] Check Availability\n"

            "What do you want to do today?: "
            )
    option = input(menu)
    if option == "":
        return
    while not option.isdigit():
        option = input("What do you want to do today?: ")

    option = int(option)

    data = pd.read_csv(path)

    if option == 0:
        add_books(data)
    elif option == 1:
        getList(data)
    elif option == 2:
        availability(data)
    else:
        print("Function not available yet")


PATH = "hellllllooo-world/data/booklist.csv"


def path_select():
    global DIVERTED_PATH
    DIVERTED_PATH = ""
    user_query = input("Who is accessing the system? ")
    if user_query.lower() in ["easton", "east"]:
        DIVERTED_PATH = "/Users/louisandeaston/Documents/GitHub/" + PATH
    elif user_query.lower() in ["eugenio", "egg"]:
        DIVERTED_PATH = PATH
    else:
        DIVERTED_PATH = PATH
    return DIVERTED_PATH


main(path_select())
while True:
    ask = input("Do you want to continue? (yes/no) ")

    if ask == "yes" or ask == "y":
        main(DIVERTED_PATH)
    else:
        break
