#!/usr/bin/env python3

"""
Author : TSuganuma

This program works with http://jservice.io
"""

import requests

ROOT_URL = "http://jservice.io"
NUM_CHANCES = 2;

def main():

    r= requests.get("http://jservice.io/api/random?count=3")
    
    #list
    jsonObj = r.json()
    
    #Get total questions
    size = len(jsonObj)

    #Reset variables
    score = 0
    currentQuestionNum = 0
    ##################### 
    
    for item in jsonObj:
        
        currentQuestionNum += 1
        
        #Print out question count
        print("Question: "+str(currentQuestionNum)+"/"+str(size))
        
        #Print out question
        print("\""+item["question"]+"\"\n")
        clueNeed =  input("Do you need a clue? (y/n): ")
        
        #Ask if a user needs a clue
        if clueNeed == "y":
            print("\""+item["category"]["title"]+"\"")
        elif clueNeed == "x":
            break;

        #-- This is for development purpose --
        print(item["answer"])

        #Reset flags
        endLooping = False
        incorrectCount = 0
        
        #Give user chances to answer
        while endLooping==False:

            ans = input("\nwhat is the answer? ")
            
            # if a user answered correctly
            if ans == item["answer"]:
                endLooping = True
                print("You are correct! You got "+ str(item["value"]), end="\n\n")
                score += item["value"]
            # if a user did not answer correctly
            else:
                print("Sorry, incorrect. Try again.")
                if incorrectCount < NUM_CHANCES:
                    incorrectCount += 1
                else:
                    print("Answer is "+ str(item["answer"]))
                    endLooping = True
    print("Your score is " + str(score))
       # print(item["value"])
       # print(item["category"]["title"])


   # print(category)
   # for categoryTitle in category:
   #     print(categoryTitle.get["title"])


if __name__ == "__main__":
    main()


