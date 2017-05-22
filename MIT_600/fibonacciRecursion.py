#!/usr/bin/python3

####################################################################
#
#  proc fibonacci by recursion
#
####################################################################

var = int(input("Enter a Number:"))

def fibonacciRe(var):
    assert type(var) == int and var >=0
    if var == 0 or var == 1:
        return 1
    else:
        return fibonacciRe(var - 1) + fibonacciRe(var - 2)

print(fibonacciRe(var))
