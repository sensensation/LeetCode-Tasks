# 1876. Substrings of Size Three with Distinct Characters
# A string is good if there are no repeated characters.
#
# Given a string s, return the number of good substrings of length three in s.
#
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
#
# A substring is a contiguous sequence of characters in a string.
#
#
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        step = 3 #step size
        ans = 0 #our counter of good substrings

        for i in range(len(s)-step+1): #the usefull cycle if you want to go for indexes with step = k

            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]: # looks difficult but it`s not, just comparing
                                                                        # all variants of 3 elements
                ans += 1   # Important! Also usefull to use syntax like += 1 instead ans = ans + 1. That faster. Remember

            return ans #return how many times our condition is satisfied
a = Solution()
print(a.countGoodSubstrings(s = "xyzzaz"))