#!/usr/bin/python3

#########################################################################
# proc hannoTower by recursion
#
########################################################################

var  = int(input("Enter HannoTower Number:"))

def hannoTower(num, fr, to, space):
    if num == 1:
        print("from",fr,"to",to)
    else:
        hannoTower(num-1, fr, space, to)
        hannoTower(1, fr , to ,space)
        hannoTower(num-1,space, to, fr)

hannoTower(var,'f','t','s')
