from timeit import default_timer as timer
import logging
import threading


# test_file = open("testing_file.txt", "a")
# for i in range(10):
#     test_file.write(str(i) + "\n")

# read = open("testing_file.txt", "r")
# print(read.read())

def add_books():
    borrowed = open("booklist.txt", "a+")

    while True:
        book = input("Enter a book name: ")
        if book.lower() == "quit":
            break

        borrowed_state = input("Has it been borrowed? ")

        while borrowed_state.lower() not in ["yes", "no"]:
            borrowed_state = input("Has it been borrowed? (yes/no) ")

        # double == makes the True/False ineffective
        borrowed_state = True if borrowed_state.lower() == "yes" else False

        borrowed.write(f"{book}: {str(borrowed_state)}\n")
        borrowed.flush()

def getList():
    readable_list = open("booklist.txt", "r")
    print("\nHere are the list of books: ")
    print(readable_list.read())

# def timeout():
#     start = timer()
#     if start == 3:
#         bool_booklist = input("Do you need the booklist? ")
#         if bool_booklist.lower() == "yes":
#             getList()
#         else:
#             pass
#         availability()

def availability():
    # time_format = "%(asctime)s: %(message)s"
    # logging.basicConfig(format=time_format, level=logging.INFO, datefmt="%H:%M:%S")
    # logging.info("Ten seconds in, there will be a prompt for a booklist.")
    # avil_start = threading.Thread(target=timeout)
    # avil_start.start()

    query = input("What book are you finding for? ")

    booklist = open("booklist.txt").readlines()
    for book in booklist:
        x = book.rsplit(maxsplit=1)
        book_name = x[0][:-1]
        book_available = x[1] == "True"

        if book_name == query:
            if book_available:
                print("Available!")
                return
            else: 
                print("Not Available")
                return
  
    print("There are no records of the book.")


def main(task):
    if task == "0":
        add_books()
    elif task == "1":
        getList()
    elif task == "2":
        availability()
    else:
        print("No such function yet.")


menu = ("hellllllooo-world:\n"
        "----------------------------------------\n"
        "Main Menu\n"
        "----------------------------------------\n"
        "[0] Add Books\n"
        "[1] Get Booklist\n"
        "[2] Check Availability\n"

        "What do you want to do today? "
        )

main(input(menu))

while True:
    ask = input("Do you want to continue? (yes/no) ")

    if ask == "yes" or ask == "y":
        main(input(menu))
    elif ask == "no" or ask == "n":
        break
