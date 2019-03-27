def countdown(num):
    retList = []

    for i in range(num, -1, -1):
        retList.append(i)
    return retList

print(countdown(5))

def printReturn(inList):
    print(inList[0])
    return inList[1]

print(printReturn([1,2]))

def firstLen(inList):
    return inList[0] + len(inList)

print(firstLen([1,2,3,4,5]))

def valuesGreater(inList):
    checkVal = inList[1]
    retList = []

    for i in range(len(inList)):
        if inList[i] > checkVal:
            retList.append(inList[i])

    return retList
print(valuesGreater([5,2,3,2,1,4]))    

def lenValue(size, value):
    retList = []
    for i in range(size):
        retList.append(value)
    return retList

print(lenValue(4,7))