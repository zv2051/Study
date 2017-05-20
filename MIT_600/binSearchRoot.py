#**************************************************************************
#* This program is only a define
#* This def is use to find root for bin-serach
#*
#*
#**************************************************************************

def binSearchRoot(number, power,epsilon):
    low = 0
    high = number
    ans = (low + high) / 2.0
    while abs(ans ** power - number) > epsilon:
        if ans ** power < number:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
    return ans
