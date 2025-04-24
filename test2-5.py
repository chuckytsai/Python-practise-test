# Write a function called "swap" that takes a string as input, and returns a new string with lowercase changed to uppercase,
# uppercase changed to lowercase.

def swap(text):
    new = ""
    for item in text:
        if(item.isupper()):
            new = str(new) + str(item.lower())
        else:
            new = str(new) + str(item.upper())

    print(new)
    return new


swap("Aloha"); # returns "aLOHA"
swap("Love you."); # returns "lOVE YOU."