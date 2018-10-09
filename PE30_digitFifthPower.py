def sumOfFifthPowersOfDigits(num):
    sum = 0
    while(num > 0):
        sum += ((num % 10) ** 5)
        num = num // 10
    return sum
#print(sumOfFifthPowersOfDigits(8208))
sum = 0
for i in range(10, 1000000):
    if sumOfFifthPowersOfDigits(i) == i:
        sum += i
print(sum)
