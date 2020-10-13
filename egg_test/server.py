import numpy as np
import pandas as pd
import os, sys
import socket
import threading
import pickle

from time import sleep

RELATIVE_PATH = "hellllllooo-world/egg_test/data/booklist.csv"
PORT = 6666
SERVER = "192.168.1.118" # set this to your own ip address

ADDR = (SERVER, PORT)

#print(os.getpid())

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

def path_select():
    path = ""

    user_query = input("Who is running the server?: ")

    while user_query not in ["easton", "east", "eugenio", "egg"]:
        user_query = input("Who is running the server?: ")
      
    
    if user_query.lower() in ["easton", "east"]:
        path = "/Users/louisandeaston/Documents/GitHub/" + RELATIVE_PATH

    elif user_query.lower() in ["eugenio", "egg"]:
        path = "C:/Users/Egie/Desktop/Projects/SonrisaProjects/" + RELATIVE_PATH

    return path

BOOKLIST_PATH = path_select()

def add_book(booklist, list_path,
            book_name, borrowed, price):

    book = [[book_name, borrowed, price]]

    new_book = pd.DataFrame(book, columns=["Book", "Borrowed", "Price"])
    booklist = booklist.append(new_book, sort=False)
    booklist.to_csv(list_path, index=False)


def getList(booklist):
    pd.set_option('display.max_rows', 1000)
    return booklist


def availability(booklist):
    available = booklist.loc[booklist["Borrowed"] == False, ["Book", "Price"]]
    return available



def client_handler(conn, addr):
    print(f"Connected to {addr}")
    query = conn.recv(12).decode("utf-8")
    print(f"Query: {query}")

    if query == "0":

        book_data_length = conn.recv(1024).decode("utf-8")
        book_data = conn.recv(int(book_data_length))

        book_data = pickle.loads(book_data)

        print(book_data)

        add_book(BOOKLIST, BOOKLIST_PATH, book_data[0], book_data[1], book_data[2])

        send_data = pickle.dumps(f"Book {book_data[0]} successfully added.")
        send_length = bytes(f"{len(send_data)}", "utf-8")

        conn.send(send_length)
        sleep(1)
        conn.send(send_data)

    elif query == "1":
        l = getList(BOOKLIST)
        
        send_data = pickle.dumps(f"Booklist:\n{l}")
        send_length = bytes(f"{len(send_data)}", "utf-8")

        conn.send(send_length)
        sleep(1)
        conn.send(send_data)

    elif query == "2":
        l = availability(BOOKLIST)
        
        send_data = pickle.dumps(f"Available books:\n{l}")
        send_length = bytes(f"{len(send_data)}", "utf-8")

        conn.send(send_length)
        sleep(1)
        conn.send(send_data)

    else:
        send_data = pickle.dumps("Function not available")
        send_length = bytes(f"{len(send_data)}", "utf-8")

        conn.send(send_length)
        sleep(1)
        conn.send(send_data) 

    

BOOKLIST = pd.read_csv(BOOKLIST_PATH)

def main():
    conn, addr = server.accept()

    client_handler(conn, addr)

main()

