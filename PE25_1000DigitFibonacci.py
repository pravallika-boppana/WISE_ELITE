def noOfDigits(num):
    return len(str(num))

def nDigitFibonacci(digit):
    term1 = 1
    term2 = 1
    term3 = 0
    count = 2
    while (digit != noOfDigits(term3)):
        term3 = term1 + term2
        term1 = term2
        term2 = term3
        count += 1
       
    return count
print(nDigitFibonacci(1000))


