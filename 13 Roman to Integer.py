# 13. Roman to Integer
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    start = 0
    for i in s[::-1]:
        if d[i] >= start:
            result += d[i]
        else:
            result -=d[i]
        start = d[i]
    return result

print(romanToInt("MCMXCIV"))




























