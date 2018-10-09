print(2 ** 1000)
def sumOfDigits(num):
    sum  = 0
    while(num > 0):
        sum += num % 10
        num = num // 10
    return sum
print(sumOfDigits(2 ** 1000))
            
