# Write a function called "palindrome" that checks if the input string is a palindrome.
# (Search on google if you don't know what a palindrome is.)

def palindrome(text):
    result = "true"
    for i, item in enumerate(text):
        if (text[i] != text[len(text) - 1 - i]):
            result = "false"

    print(result)
    return True


palindrome("bearaeb")  # true
palindrome("Whatever revetahW")  # true
palindrome("Aloha, how are you today?")  # false
