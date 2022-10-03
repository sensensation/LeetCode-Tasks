# 922. Sort Array By Parity II
# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
#
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
#
# Return any answer array that satisfies this condition.
def sortArrayByParityII(nums):
    l, r = 0, len(nums) - 1

    while l < len(nums) and r > 0:

        if nums[l] % 2 == 0:
            l += 2

        elif nums[r] % 2 != 0:
            r -= 2

        else:
            nums[l], nums[r] = nums[r], nums[l]
            l += 2
            r -= 2

    return nums

print(sortArrayByParityII(nums = [4,2,5,7]))