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
    modus = False
    while not modus:
        include_book = input("Enter a book name: ")
        if include_book.lower() == "quit":
            break
        while True:
            borrowed_state = input("Has it been borrowed? ")
            if borrowed_state.lower() == "yes":
                borrowed_state = True
                break
            elif borrowed_state.lower() == "no":
                borrowed_state = False
                break
            else:
                continue
        borrowed.write(f"{include_book}: {str(borrowed_state)}\n")
        borrowed.flush()

def getList():
    readable_list = open("booklist.txt", "r")
    print("Here are the list of books: ")
    print(readable_list.read())

def timeout():
    start = timer()
    if start == 3:
        bool_booklist = input("Do you need the booklist? ")
        if bool_booklist.lower() == "yes":
            getList()
        else:
            pass
        availability()

def availability():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Ten seconds in, there will be a prompt for a booklist.")
    avil_start = threading.Thread(target=timeout)
    avil_start.start()
    available = input("What book are you finding for? ")
    with open("booklist.txt") as check_availability:
        for num, line in enumerate(check_availability):
            temp = line.split()
            while True:
                if ":" not in temp[0]:
                    more_temp = temp[0] + " " + temp[1]
                    temp.pop(0)
                    temp.pop(0)
                    temp.insert(0, more_temp)
                else:
                    break
            if available in temp[0]:
                boolean = temp[1]
                if boolean == "True":
                    print("Available!")
                    break
                else:
                    print("Not available.")
                    break
            else:
                boolean = None
        if boolean is None:
            print("There are no records of the book.")

def __main__(user):
    if user.lower() == "add books":
        add_books()
    elif user.lower() == "get booklist":
        getList()
    elif user.lower() == "check availability":
        availability()
    else:
        print("No such function yet.")

__main__(input("What do you want to do today? "))
while True:
    ask = input("Do you want to continue? ")
    if ask == "yes":
        __main__(input("What do you want to do today? "))
    else:
        break
