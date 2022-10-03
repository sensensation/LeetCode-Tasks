# 718. Maximum Length of Repeated Subarray
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
def findLength(nums1, nums2):
    double = []
    tmp = []
    for i in nums1:
        if i in nums2:
                double.append(i)
    counter = 1
    for x in double:
        if x not in tmp:
            tmp.append(x)
        else:
            counter += 1
    result = max(counter,len(tmp))

    print(result)


findLength([1,2,3,2,1], [3,2,1,4,7])













