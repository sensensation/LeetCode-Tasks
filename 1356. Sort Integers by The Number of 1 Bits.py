#1356. Sort Integers by The Number of 1 Bits

def sortByBits(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))












