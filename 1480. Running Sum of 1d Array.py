#1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        cursum = int()
        for i in nums:
            cursum += i
            ans.append(cursum)
        return ans
            