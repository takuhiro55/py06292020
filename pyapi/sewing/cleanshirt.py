#!/usr/bin/env python3

import threading
import time

def groundcontrol():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)

print("Orion, you are primed for launch. Count down begins...")

## Create a thread object (target is the function to call)
mythread = threading.Thread(target=groundcontrol)

## begin the thread
mythread.start()

## Ask the user to press any key to exit.
input("Press Enter to exit.")
exit()
