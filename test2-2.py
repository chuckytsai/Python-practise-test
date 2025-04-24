# Write a function called "stars2" which prints out layers of stars in the following pattern:

def stars2(num):
    # for item in range(1, (num + 1) + (num - 1)):
    #     if (item <= num):
    #         print(num, "*" * item)
    #     else:
    #         print(num, "*" * ((num - item) + num))
    for item in range(1, num + 1):
        print(num,"*" * item)
    for item in range(num - 1, 0, -1):
        print(num,"*" * item)


stars2(1)
# *
stars2(2)
# *
# **
# *
stars2(3)
# *
# **
# ***
# **
# *
stars2(4)
# *
# **
# ***
# ****
# ***
# **
# *
