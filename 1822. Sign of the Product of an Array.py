#1822. Sign of the Product of an Array
# There is a function signFunc(x) that returns:
#
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
#
# Return signFunc(product).
import math
def arraySign(nums):
    desicion = 0
    pow = math.prod(nums)
    if pow == 0:
        desicion = 0
    elif pow >= 0:
        desicion = 1
    else:
        desicion = -1

    return desicion

bebra = [-1]
print(arraySign(bebra))







