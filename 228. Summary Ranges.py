# 228. Summary Ranges
# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b
# nums = [0,1,2,4,5,7]

def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    ans, i = [], 0  # take i to traverse the array, ans to fill the ranges
    while i < len(nums):  # traverse the array
        lower = upper = nums[i]  # for a range we need to find the upper and lower values
        while i < len(nums) and nums[i] == upper:  # increment the i and upper as well in order to check they are equal.
            i += 1
            upper += 1
        ans.append(str(lower) + ("->" + str(
            upper - 1) if upper - lower - 1 else ""))  # if upper-1 and lower both are equal append only lower, else append the range
    return ans



nums = [0,1,2,4,5,7]
print(summaryRanges(nums))























