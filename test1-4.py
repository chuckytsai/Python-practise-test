# Write a function called "findSmallCount" that takes one list of integers and one integer as input, 
# and returns an integer indicating how many elements in the list is smaller than the input integer.
def findSmallCount(args, nums):
   print(len([item for item in args if item < nums]))
   return len([item for item in args if item < nums])

findSmallCount([1, 2, 3], 2); # returns 1
findSmallCount([1, 2, 3, 4, 5], 0); # returns 0