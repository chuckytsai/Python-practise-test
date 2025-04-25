# Write a function called "isPrime" that takes an integer as input,
# and returns a boolean value that indicates if the input number is prime.

def isPrime(num):
    if num == 1:
        print(False)
        return False

    starter = 2
    while starter < num:
        if num % starter == 0:
            print(False, starter)
            return False
        starter += 1

    print(True)
    return True


isPrime(1)  # returns false
isPrime(5)  # returns true
isPrime(91)  # returns false
isPrime(1000000)  # returns false
