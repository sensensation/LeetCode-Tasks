#775. Global and Local Inversions
# You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].
#
# The number of global inversions is the number of the different pairs (i, j) where:
#
# 0 <= i < j < n
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution(object):

    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        letters = []
        for i in stones:
            letters.append(i)

        result = [x for x in letters if x in jewels]
        return len(result)




