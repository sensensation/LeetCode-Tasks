# 179. Largest Number
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            m = i
            m_str = str(nums[i])
            for j in range(i + 1, len(nums)):

                j_str = str(nums[j])
                # Create XY AND YX and then compare.
                first_num = m_str + j_str
                second_num = j_str + m_str

                if first_num < second_num:
                    m = j
                    m_str = str(nums[m])
            nums[i], nums[m] = nums[m], nums[i]
        if nums[0] == 0:
            return "0"
        return "".join([str(x) for x in nums])





