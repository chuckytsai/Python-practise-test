# Write a function called "mySort" that takes an list of integers as input, and returns the sorted version of the input list.
# You are not allowed to use the built-in sorted() function.

def mySort(lst):
    new = lst
    for i, item in enumerate(lst):
        for (j, items) in enumerate(new):
            if (item < items):
                new[i], new[j] = new[j], new[i]

    print(new)
    return new

mySort([17, 0, -3, 2, 1, 0.5])  # returns [-3, 0, 0.5, 1, 2, 17]
