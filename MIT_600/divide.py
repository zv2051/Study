#!/usr/bin/python3
###########################################################################
#This program is study how to use except
#
#
###########################################################################

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print("divison by zero!", e)
    except TypeError as e:
        divide(int(x), int(y))
    else:
        print("result=", result)
    finally:
        print("execuing finally clause")
