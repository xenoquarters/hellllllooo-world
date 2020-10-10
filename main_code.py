import numpy as np

def add_books():
    borrowed = open("list/booklist.txt", "a+")

    while True:
        book = input("Enter a book name (Type 'Quit' to stop): ")
        if book.lower() == "quit":
            break

        borrowed_state = input("Has it been borrowed? ")

        while borrowed_state.lower() not in ["yes", "no"]:
            borrowed_state = input("Has it been borrowed? (yes/no) ")

        borrowed_state = True if borrowed_state.lower() == "yes" else False

        borrowed.write(f"{book}: {str(borrowed_state)}\n")
        borrowed.flush()

def getList():
    booklist = open("list/booklist.txt", "r").readlines()
    booklist = np.array([[x.split(":")[0], x.strip().split(":")[1]] for x in booklist])
    
    align = max(map(len, booklist[:, 0])) + 10
    print("\nHere are the list of books: ")
    print("Book", "Borrowed".rjust(align-4))
    for book in booklist:
        print(book[0], book[1].rjust(align-len(book[0])))


def availability():
    query = input("What book are you finding for? ")
    booklist = open("list/booklist.txt").readlines()
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

# so much easier if it's in java with get and set attributes
def setPrice():
    query = input("Which book do you want to set a price to? ")
    book_price = ""
    while not isinstance(book_price, float):
        book_price = input("Enter a price for the book: ")

    """
    saving this part for someday when i do this bc i would like to have a portion where it includes the price,
    but it'll mess up the code for availability() and i might consider doing a csv file so yea
    
    essentially if we're sticking to text files, the format would be like:
    xinmin: True, price: $3.50
    and there'll be a shit ton of appending and trying to extract the value and many splits
    
    i thought of using rsplit(maxsplit: 2) 2 times to get the name of the book and the price so maybe
    i'll convert the booklist to a csv file if i have the time for that
    
    also i might do an authentication thingy where a password is needed in order to set the price so it's kinda like
    admin rights and we can implement that in main()
    """


def getPrice():
    pass


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
