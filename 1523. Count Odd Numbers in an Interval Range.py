# 1523. Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
def countOdds(self, low: int, high: int) -> int:
    if (high - low + 1) % 2 == 0:
        return (high - low + 1) // 2
    elif high % 2 == 0 and low % 2 == 0:
        return (high - low) // 2
    else:
        return (high - low) // 2 + 1