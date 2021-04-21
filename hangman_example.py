'''
nci programme: BSHDS week 5
program: hangman
author: Renato Gusani
studentID: x19411076
date: 23/02/2020

'''

import random #picks random word from below answerlist

answerlist = ["earth," "mars", "venus", "saturn"]

random.shuffle(answerlist)

answer = list(answerlist[0])

#empty list named display
display = []

display.extend(answer)

#reccurence through the list 'display'

for i in range (len(display)):
    #each index in the list uses ' _ '
    display[i] = " _ "

    #join command inserts a space between each ' _ '
    print (' '.join(display))
    print()

    #tally stops the game once all letters for the word have been guessed
    count = 0

    #ask player for letters until all correctly guessed (while loop)
    while count < len(answer):
        guess = input("input any letter: ")
        guess = guess.lower()
        print (count)

        #runs through the letters in answer
        for i in range(len(answer)):
            # if guess is correct
            # matches in answer
            display[i] = guess
            count = count + 1

            #prints out new string with guessed letters
            print (' '.join(display))
            print()

            print("you win! you guessed the word!")

            # program not finished