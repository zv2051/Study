#!/usr/bin/python3

############################################################################
#  This is a test
#  Use recursion make product
###########################################################################

print("This program is product by recursion")

varA = int(input("Enter numberA:"))
varB = int(input("Enter numberB:"))
#print(varA,varB)
result = 0
def reProduct(varA, varB):
    if varB == 1:
        return varA
    else:
        return varA + reProduct(varA, varB-1)
print(reProduct(varA,varB))
