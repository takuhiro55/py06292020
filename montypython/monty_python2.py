#!/usr/bin/env python3
'''
Lab 19 - Using while, if, elif, else
'''

correctAns = 'Brian'

def main():
    round = 0
    while True:
        round = round + 1
        print("Finish the movie title,'Monty Python\'s The Life of ____ ")
        answer = input("Your guess-->");
        if answer == correctAns.lower() or answer == correctAns.upper():
            print('Correct!')
            break;
        elif answer == 'shrubbery':
            print('You gave the super secret answer!')
            break;
        elif round == 3:
            print('Sorry, the answer was Brian')
            break;
        else:
            print('Sorry. Try again')

if __name__ == "__main__":
    main()

