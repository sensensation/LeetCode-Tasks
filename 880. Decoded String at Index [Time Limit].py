def decodeAtIndex(self, s: str, k: int) -> str:
    buffer = ""
    for i in range(0, len(s)):
        if s[i].isalpha():
            buffer += s[i]
        else:
            b = int(s[i])
            buffer = (b * buffer)

    return buffer[k - 1]
#print(decodeAtIndex(s = "leet2code3", k = 10))
#print(decodeAtIndex(s = "ha22", k = 5))
print (decodeAtIndex("a2345678999999999999999", k = 1))

