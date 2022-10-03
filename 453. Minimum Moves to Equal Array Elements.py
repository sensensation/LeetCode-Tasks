# 453. Minimum Moves to Equal Array Elements
def minmoves(nums):
    minimum = min(nums)
    print(minimum)
    return print(sum(num - minimum for num in nums))



minmoves(nums = [1,2,3])