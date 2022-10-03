# 239. Sliding Window Maximum
#Sliding window
import collections
def maxSlidingWindow(nums,k):
    output = []
    q = collections.deque() #index
    l = r = 0

    while r < len(nums):
        #pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left value from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1

        r += 1

    return output

print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))