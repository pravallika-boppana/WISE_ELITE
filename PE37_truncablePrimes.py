import math
def reverse(num):
    rev = 0
    while(num > 0):
        rev = rev * 10 + num % 10
        num //= 10
    return rev
print("reverse 7893:",reverse(7893))
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def isLeftTruncatable(num):
    while(num > 0):
        #print(num)
        if(isPrime((num)) == False):
            return False
        num = reverse(num)
        num = num // 10
        num = reverse(num)

    return True

def isRightTruncatable(num):
    while (num > 0):
        #print(num)
        if (isPrime(num) == False):
            return False
        
        num  = num // 10
    return True
print(isRightTruncatable(3797))
print(isLeftTruncatable(3797))

count = 0
sum = 0
i = 11
while(count < 11):
    
    if (isLeftTruncatable(i) and isRightTruncatable(i)):
        sum += i
        count += 1
        print("i, count:",i,count)
    i += 1
print("sum:",sum)



