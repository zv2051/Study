#!/usr/bin/python3

###################################################################
#
# str to float.  "123.00"  to  123.00
#
###################################################################

from functools import reduce

def str2int(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}[s]
def str2float(s):
    l = s.split(".")
    l[1] = l[1][::-1]
    return reduce(lambda x,y:x*10+y,map(str2int,l[0])) + reduce(lambda x,y:x*0.1+y, map(str2int,l[1]))*0.1
