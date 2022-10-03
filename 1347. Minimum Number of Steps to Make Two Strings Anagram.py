# 1347. Minimum Number of Steps to Make Two Strings Anagram
#
# You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
#
# Return the minimum number of steps to make t an anagram of s.
#
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.
import collections
def minSteps(self, s, t):
    return sum((collections.Counter(s) - collections.Counter(t)).values())