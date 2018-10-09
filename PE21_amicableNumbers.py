def sumOfDivisors(num):
    sum = 1
    for i in range(2, num // 2 + 1):
        if n % i == 0:
            sum += i
    return sum
