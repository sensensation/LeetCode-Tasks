# 1984. Minimum Difference Between Highest and Lowest of K Scores
# You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
#
# Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
#
# Return the minimum possible difference.
#
#

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[k-1] - nums[0]
        for i in range(0, len(nums)-k+1):
            if nums[i+k-1] - nums[i] < ans:
                ans = nums[i+k-1] - nums[i]
        return ans