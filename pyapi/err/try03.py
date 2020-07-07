#!/usr/bin/env python3

#Start with an infinite loop
while True:
    try:
        print("\nLet's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as err:
        print("Handling run-time error:", err)
    except ValueError as err:
        print("That was not a legal value for division:", err)

    except Exception as err:
        print("We did not anticipate that:", err)
        ## raise by itself simply calls the previous exception that was thrown
        raise

    else:
        print("\nThanks for learning to handle errors!")
        break
