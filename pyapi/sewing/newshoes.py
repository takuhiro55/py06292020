#!/usr/bin/python3

import threading
import time

def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

## Create a thread object (target is the function to call)
mythread = threading.Thread(target=groundcontrol)

## begin the thread
mythread.start()

print("Oh no, I forgot socks!")

# Wait until the threads finish before moving on.
mythread.join()

## Ask the user to press any key to exit.
input("Press Enter to exit.")
exit()
