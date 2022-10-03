# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#
#

import itertools


def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pairs = 0
    for x, y in itertools.combinations(nums, 2):
        if x == y:
            pairs += 1


    return pairs