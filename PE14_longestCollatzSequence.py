def lengthOfCollatzSequence(start):
    length = 1
    while (start > 1):
        if (start % 2 == 1) :
            start = start * 3 + 1
        else:
            start = start // 2
        length += 1 
    return length
#print(lengthOfCollatzSequence(837799))
maxLength = 0
maxStart = 0
l = []
for i in range(1, 1000000):
    l.append(lengthOfCollatzSequence(i))
    if lengthOfCollatzSequence(i) > maxLength:
        maxLength = lengthOfCollatzSequence(i)
        maxStart = i
print(maxStart)

