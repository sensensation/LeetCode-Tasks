# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
class Solution:
    def maxSubArray(self, nums) -> int:
        self.nums = nums
        curSum = 0
        maxSub = nums[0]

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)
        return maxSub

a = Solution()
print(a.maxSubArray(nums = [5,4,-1,7,8]))