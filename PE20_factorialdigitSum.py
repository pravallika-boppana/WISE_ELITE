def sumOfDigits(num):
    sum = 0
    while(num > 0):
        sum += num % 10
        num //= 10
    return sum
def factorial(num):
    result = num
    for i in range(2, num):
        result *= i
    return result
print(sumOfDigits(factorial(100)))
