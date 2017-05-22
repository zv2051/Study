#!/usr/bin/python3

####################################################################
#
#  test palindrome string by recursion
#
####################################################################

var = input("enter string: ")

def testPal(var):
    def toChar(string):
        string = string.low()
        ans = ''
        for c in string:
            if c in "abcdefghijklmnopqrstuvwxyz0123456789":
                ans += c
        return ans
    def isPal(string):
        if len(string) <= 1:
            return True
        else:
            return string[0] == string[-1] and isPal(string[1:-1])
    return isPal(toChar(var))
print(testPal(var))
