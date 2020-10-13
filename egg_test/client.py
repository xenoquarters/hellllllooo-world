import numpy as np
import pandas as pd
import os, sys
import socket
import threading
import pickle

from time import sleep

RELATIVE_PATH = "hellllllooo-world/egg_test/data/booklist.csv"
PORT = 6666
SERVER = "192.168.1.118" # set this to the ip address that your server.py is running on

ADDR = (SERVER, PORT)

menu = ("----------------------------------------\n"
            "Main Menu\n"
            "----------------------------------------\n"
            "[0] Add Books\n"
            "[1] Get Booklist\n"
            "[2] Check Availability\n"

            "What do you want to do today?: "
            )

def main():
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    client.connect(ADDR)

    query = input(menu)

    while query.isdigit() == False:
        query = input("What do you want to do today?: ")

    if query == "0":
        book_name = input("Enter name of book: ")
        borrowed = input("Has it been borrowed?: ")
        price = input("Price of item: ")

        while borrowed.lower() not in ["yes", "no", "y", "n"]:
            borrowed = input("Has it been borrowed? (yes/no): ")

        if borrowed.lower() in ["y", "yes"]:
            borrowed = True
        else:
            borrowed = False
        
        send_data = pickle.dumps([book_name, borrowed, price])
        send_data_length = bytes(f"{len(send_data)}","utf-8")

        client.send(bytes(query, "utf-8"))
        sleep(1)
        client.send(send_data_length)
        sleep(1)
        client.send(send_data)

    else:
        client.send(bytes(query, "utf-8"))
    
    recv_length = client.recv(1024).decode("utf-8")
    recv_data = client.recv(int(recv_length))
    
    recv_data = pickle.loads(recv_data)
    print(recv_data)

main()


