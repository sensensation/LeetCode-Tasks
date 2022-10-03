#443. String Compression
# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.

def compress(chars) -> int:
    comp_str = ''
    c = 1

    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
            c += 1
        else:
            comp_str += chars[i] + str(c)
            c = 1
    comp_str += chars[i] + str(c)
    if len(comp_str) >= len(chars):
        return chars
    else:
        return len(comp_str)




print(compress(chars = ["a","a","b","b","c","c","c"]))
