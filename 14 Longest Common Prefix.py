# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#  strs = ["flower","flow","flight"]
def longestCommonPrefix(strs):
    # Sort the list with shortest words first (helps reduce runtime, even if the solution works without it)
    strs.sort(key=len)
    # While the first word in the list is not ""
    while strs[0]:
        # Counter variable used to check if program execution can be ended or not
        count = 0
        # Go through list of words
        for i in range(0, len(strs)):
            # If first word does not prefix another, break loop
            if not strs[i].startswith(strs[0]):
                break
            # If first word prefixes the next, increment counter variable by 1
            if strs[i].startswith(strs[0]):
                count += 1
            # If counter variable is equal to length of list
            # Then all words are prefixed by our first word
            # Which means that the first word is the answer
            if count == len(strs):
                return strs[0]
        # If the first word does not prefix the others, remove its last letter and try again
        strs[0] = strs[0][:len(strs[0]) - 1]
    # If no prefix exists, return strs[0], which is "" by this point
    return strs[0]

print(longestCommonPrefix(['flower', 'flow', 'flight']))
