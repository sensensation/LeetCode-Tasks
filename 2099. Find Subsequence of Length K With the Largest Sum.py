#2099. Find Subsequence of Length K With the Largest Sum
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
import itertools as it

def maxSubsequence(nums,k):
    res = []
    combos = list(it.combinations(nums, k))
    sums = list(map(sum, combos))
    print(combos)
    print(sums)
    g = max(list(map(sum, combos)))
    print(g)
    ans = sums.index(g)
    print(ans)
    for i in combos[ans]:
        res.append(i)

    return print(res)






#maxSubsequence(nums = [2,1,3,3], k = 2)
#maxSubsequence([-1,-2,3,4], k = 3)
#maxSubsequence(nums = [3,4,3,3], k = 2)
maxSubsequence([-76,-694,44,197,357,-833,-277,358,724,-585,-960,214,465,-593,-431,625,-83,58,-889,31,765,8,-17,476,992,803,863,242,379,561,673,526,-447],
14)













