#1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
def longestOnes(nums, k: int) -> int:
    count = 0
    res = 0
    left = 0
    # 1. In
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        # 2 out.
        while count > k:
            if nums[left] == 0:
                count -= 1

            left += 1

        # 3 compute

        res = max(res, i - left + 1)

    return res








