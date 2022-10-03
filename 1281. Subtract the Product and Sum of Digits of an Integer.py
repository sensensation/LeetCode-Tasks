#1281. Subtract the Product and Sum of Digits of an Integer
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

def subtractProductAndSum(n: int) -> int:
    b = list(map(int, str(n)))
    global summ
    global pro
    summ = 0
    pro = 1
    for i in b:
        summ += i
        pro = pro * i

    print(b)
    print(summ)
    print(pro)
    return print((pro - summ))


subtractProductAndSum(234)
