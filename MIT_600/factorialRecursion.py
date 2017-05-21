#!/usr/bin/python3

####################################################################
# This is a test program
# factorial by recursion
####################################################################

print("This is a program to factorial by recursion")

var = int(input("Enter a Number(>0):"))

def facRecursion(var):
    if var == 1:
        return var
    else:
        return var * facRecursion(var - 1)

print(facRecursion(var))
