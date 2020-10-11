import time
from math import trunc
import logging
import threading

start = time.process_time()

def hello():
    ask = input("wejrhwe: ")

x = threading.Thread(target=hello)
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
logging.info("qwertyuio")

hello()
if trunc(start) == 3:
    print("hello")
print(start)