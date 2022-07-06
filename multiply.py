# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/06/2022
# Description: A recursive function that takes two positive integers as parameters
# and returns the product of those two numbers.

def multiply(x, y):
    if y == 0:
        return 0
    elif y < 0:
        return - (x - multiply(x, y + 1))
    else:
        return x + multiply(x, y - 1)

