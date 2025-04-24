# Write a function called "findSmallerTotal" that takes one list of integers and one integer as input, and returns the sum of all elements in the list that are smaller than the input integer. Write a function called "findSmallerTotal" that takes one list of integers and one integer as input, 
# and returns the sum of all elements in the list that are smaller than the input integer. 

def findSmallerTotal(args, nums):
    result = 0
    for i, num in enumerate(args):
        if(num < nums):
            result += num
   
    print(result)
    return result

findSmallerTotal([1, 2, 3], 3) # returns 3
findSmallerTotal([1, 2, 3], 1) # returns 0
findSmallerTotal([3, 2, 5, 8, 7], 999) # returns 25
findSmallerTotal([3, 2, 5, 8, 7], 0) # returns 0