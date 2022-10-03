# 374. Guess Number Higher or Lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n

        while low <= high:
            mid = (high + low) // 2
            tmp = guess(mid)

            if tmp == 0:
                return mid
            elif tmp == 1:
                low = mid + 1
            else:
                high = mid - 1




