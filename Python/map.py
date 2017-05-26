#!/usr/bin/python3

##############################################################
#
# Try use map(),make 'abC' to 'Abc'
#
#############################################################

def testMap(s):
    if len(s) >= 1:
        s = s.lower()
        s = s[0].upper() + s[1:]
        return s
    else:
        return s

l = ['heLLO', 'worLD']
result = list(map(testMap, l))
print(result)
