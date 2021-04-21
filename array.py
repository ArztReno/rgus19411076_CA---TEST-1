'''
nci programme: BSHDS week 5
program: array for lambda example
author: Renato Gusani
studentID: x19411076
date: 19/02/2020

'''

array_nums1 = [1, 3, 2, 9, 1, 2, 10, 0] # set of numbers for array 1

array_nums2 = [4, 7, 8, 2, 3] # set of numbers for array 2

print("default arrays 1 & 2: ")

print(array_nums1) # shows array1
print(array_nums2) # shows array2

result = list(filter(lambda x: x in array_nums1, array_nums2))  # using lambda method to filter out numbers in arrays

print ("\nIntersection of the arrays: ",result) # shows the intersection of both arrays