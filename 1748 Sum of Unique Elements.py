#1748 Sum of Unique Elements
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
#
# Return the sum of all the unique elements of nums.
# https://leetcode.com/problems/sum-of-unique-elements/
def sumOfUnique(nums):
    ans = []
    for i in nums:
        if nums.count(i) == 1:
            ans.append(i)

    return sum(ans)







