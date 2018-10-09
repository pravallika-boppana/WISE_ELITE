def factorial(num):
    if num == 0:
        return 1
    f = num
    for i in range(2, num):
        f *= i
    return f


def sumOfFactorialOfDigits(num):
    sum = 0
    while (num > 0):
        sum += factorial(num % 10)
        num = num // 10
    return sum
def isCuriousNumber(num):
    return num == sumOfFactorialOfDigits(num)

sum = 0
for i in range(3, 1000000):

    if isCuriousNumber(i):
        sum += i
print(sum)
            
