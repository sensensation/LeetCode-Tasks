# 1493. Longest Subarray of 1's After Deleting One Element
# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start, maxwindow, onescount = 0, 0, 0

        for end in range(len(nums)):
            onescount += nums[end]

            if (end - start + 1 - onescount) > 1:
                onescount -= nums[start]
                start += 1

            maxwindow = max(maxwindow, end - start + 1)

        return maxwindow - 1