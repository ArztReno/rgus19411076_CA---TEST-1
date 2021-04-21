'''
nci programme: BSHDS week 5
program: fibonacci sequence with recursion
author: Renato Gusani
studentID: x19411076
date: 19/02/2020

'''

def gen_seq(length):
    if(length <= 1):
        return length
    else:
        return (gen_seq(length-1) + gen_seq(length-2))
length = int(input("input amount of terms: ")) # user types in any number small or large but if too big or letter found then error 

# tested up to term of 1,000

print("Ffibonacci order :") # from what the user inputs from the previous line, here it converts the term to the fibonacci order using recursion
for iter in range(length):
    print(gen_seq(iter))