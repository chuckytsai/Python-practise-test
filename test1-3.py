# Write a function called "position" that returns a tuple of the first uppercase letter and its index location. 
# If not found, returns -1.

def position(text):
    # new = [item for item in enumerate(text) if item[1].isupper()]
    # if(len(new) > 0):
    #     idx, texts = new[0]
    #     return texts, idx
    # else:
    #     return -1

    for num, s in enumerate(text):
        if s == s.upper():
            return (s, num)
    return -1


position("abcd")  # returns -1
position("AbcD")  # returns ('A', 0)
position("abCD")  # returns ('C', 2)