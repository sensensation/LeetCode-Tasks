# 937. Reorder Data in Log Files
# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
#
# There are two types of logs:
#
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:
#
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.
def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    a = []
    b = []

    for i in logs:
        if i.split()[1].isalpha():
            a.append(i)
            print(f'a {a}')
        else:
            b.append(i)
            print(f'b = {b}')


        a.sort(key=lambda x: (x.split()[1:len(x)], x.split()[0]))
    return a + b

print(reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
