# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

import random
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    s = None
    while s != target:
        global a
        global b
        a = random.randint(0, len(nums) - 1)
        b = random.randint(0, len(nums) - 1)
        if a != b:
            s = nums[a] + nums[b]
        else:
            s = None

    result.append(a)
    result.append(b)

    print(a)
    print(b)
    print(s)





    return print(result)
twoSum([3,3],6)

twoSum([3,2,3],6)

twoSum([2,7,11,15],9)

twoSum([0,4,3,0],0)































