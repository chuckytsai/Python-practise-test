# Write a function called "stars" which prints out layers of stars in the following pattern:

def stars(num):
    for item in range(1, num + 1):
        print(num,"*" * item)
    

stars(1);
# *
stars(4);
# *
# **
# ***
# ****