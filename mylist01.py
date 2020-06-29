#!/usr/bin/python3
# Above path is getting from when you type 'which python3'

'''
Author : 
This is multiline comments
'''

# All programs should be inside of functions
# We are defining function with def
def main():
    movies = [] # one way to create a list
    movies.append("Avatar") #.append is a list method that applies the value
    # passed to it at the END of the list
    movies.append("Back to the Future")
    print(movies) # use the print FUNCTION to display to std out

    # We would like to print out only first index
    print(movies[0])

    # We would like to add another movie
    movies.append("Ghostbusters") 
    
    # We would like to print Ghostbusters
    print('Index=2: '+ movies[2])
    print(movies[-1])
    print(movies.index("Ghostbusters"))
    print(movies[movies.index("Ghostbusters")])

#Zach says this is the best way to run the main function
#This is not true for importing methods
if __name__ == "__main__":
    main()



