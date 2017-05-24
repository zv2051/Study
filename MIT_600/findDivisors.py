#!/usr/bin/python3

#############################################################################
#
#input n1 & n2, find numbers its can divisor n1 and n2
#
############################################################################

def findDivisors(number1, number2):
    result = ()
    for i in range(1,min(number1, number2)):
        if number1 % i == 0 and number2 % i == 0:
            result += (i,)
    return result
