#2099. Find Subsequence of Length K With the Largest Sum
# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that
# has the largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing
# the order of the remaining elements.
def maxSubsequence(nums,k):
    ans = []
    a = list(enumerate(nums.copy()))
    # print(a)

    a = sorted(a, key=lambda x: x[1], reverse=True)
    print(a)

    for i in range(k):
        ans.append(a[i])
    print(ans)

    ans.sort()
    print(ans)

    res = []

    for index in range(len(ans)):
        res.append(ans[index][1])

    return print(f'answer is ', res)

maxSubsequence([63,-74,61,-17,-55,-59,-10,2,-60,-65],9)
# maxSubsequence(nums = [2,1,3,3], k = 2)
# maxSubsequence([-1,-2,3,4], k = 3)
# maxSubsequence(nums = [3,4,3,3], k = 2)
# maxSubsequence([-76,-694,44,197,357,-833,-277,358,724,-585,-960,214,465,-593,-431,625,-83,58,-889,31,765,8,-17
# ,476,992,803,863,242,379,561,673,526,-447],14)
# maxSubsequence([3,4,3,3,5,6,7,8],k=3)
# maxSubsequence(nums = [-75,50], k = 2)
# maxSubsequence([-8,-94,-30,-98,-27,62,26],k=7)












