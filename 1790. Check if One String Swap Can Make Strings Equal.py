#1790. Check if One String Swap Can Make Strings Equal
# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string
# (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    step, pos1, pos2, s = 0, -1, -1, ''
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            step += 1
            if step > 2:
                return 0

            if pos1 == -1:
                pos1 = i
            else:
                pos2 = i

    for i in range(len(s1)):
        if i == pos1:
            s += s1[pos2]
        elif i == pos2:
            s += s1[pos1]
        else:
            s += s1[i]

    return s == s2









