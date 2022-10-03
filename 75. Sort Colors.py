#75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    red = nums.count(0)
    white = nums.count(1)
    blue = nums.count(2)

    for i in range(0, red):
        nums[i] = 0
    for i in range(red, white + red):
        nums[i] = 1
    for i in range(white + red, white + red + blue):
        nums[i] = 2

    return nums
