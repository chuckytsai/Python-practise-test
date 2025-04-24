# Write a function called "table" which takes an input n, and prints out n x 1 to n x 9

def table(num):
    for item in range(1, 10):
        print(f"{num} * {item} = {item * num}")

table(3);
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 9 = 27