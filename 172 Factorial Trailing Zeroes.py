#172. Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
import math
n = 100
saver = []
factorial = math.factorial(n)
listed = list(map(int, str(factorial)))

for item in listed[::-1]:
    if item == 0:
        saver.append(item)
    else:
        continue

print(len(saver))
print(math.factorial(n))
print(factorial)
print(listed)






