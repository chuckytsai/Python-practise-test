# Write a function called "table9to9" that prints out the multiplication table:
def table9to9():
    for main in range(1, 10):
        for send in range(1, 10):
            print(f"{main} * {send} = {main * send}")
    

table9to9();
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 1 x 9 = 9
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 9 x 9 = 81