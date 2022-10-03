#976. Largest Perimeter Triangle
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
# formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
def largestPerimeter(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = sorted(nums)
    for i in range(len(nums) - 3, -1, -1):
        if a[i] + a[i + 1] > a[i + 2]:
            return print(a[i] + a[i + 1] + a[i + 2])
    return print('0')


largestPerimeter(nums = [2,1,2])