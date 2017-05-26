#!/usr/bin/python3

#######################################################################
#
# Try to use reduce
#
######################################################################

from functools import reduce

def prod(L):
    return reduce(lambda x,y: x * y, L)

print(prod([1,2,3,4,5,6,7,8,9]))
