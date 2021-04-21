'''
nci programme: BSHDS week 5
program: sorting string lowercase first then upper case
author: Renato Gusani
studentID: x19411076
date: 21/02/2020

'''

inputStr = "PyNaTiveCOde" # this is the string the program will recognise and reverse in terms of lowercase first then uppercase after
words = inputStr.split() # splits the input string into 2 sections
lower = [] # stores lowercase characters
upper = [] # stores uppercase characters
for char in inputStr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedString = ''.join(lower + upper)
print("\n string characters lowercase letters coming first:")
print(sortedString) # shows the string after it has been sorted starting from lowercase