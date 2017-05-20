#**************************************************************************
#* This program is only a define
#* This def is use to find root for bin-serach
#*
#*
#**************************************************************************

def binSearchRoot(number, power,epsilon):
    if number < 0 and power%2 == 0:
	return None
    low = min(-1,number)
    high = max(1,number)
    ans = (low + high) / 2.0
    while abs(ans ** power - number) > epsilon:
        if ans ** power < number:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
    return ans
