#905. Sort Array By Parity
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.
def sortArrayByParity(nums):
    ans = []
    for i in nums:
        if i % 2 == 0:
            ans.append(i)
    for i in nums:
        if not i % 2 == 0:
            ans.append(i)

    return ans








