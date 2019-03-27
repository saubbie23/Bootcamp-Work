def biggieSize(inList):
    for i in range(len(inList)):
        if inList[i] > 0:
            inList[i] = "big"
    return inList
print(biggieSize([-1,3,5,-5]))    

def countPos(inList):
    numPos = 0
    for i in range(len(inList)):
        if inList[i] > 0:
            numPos += 1
    inList[len(inList)-1] = numPos
    return inList

print(countPos([-1,1,1,1]))        

def sumTotal(inList):
    sum = 0
    for i in range(len(inList)):
        sum += inList[i]
    return sum

print(sumTotal([1,2,3,4]))

def avg(inList):
    sum = 0
    for i in range(len(inList)):
        sum += inList[i]
    return sum / len(inList)

print(avg([1,2,3,4]))    

def length(inList):
    return len(inList)

print(length([37,2,1,-9]))    

def minimum(inList):
    if len(inList) == 0:
        return False
    else:    
        min = inList[0]

        for i in range(len(inList)):
            if inList[i] < min:
                min = inList[i]
        return min

print(minimum([37,2,1,-9]))
print(minimum([]))

def maximum(inList):
    if len(inList) == 0:
        return False
    else:
        max = inList[0]

        for i in range(len(inList)):
            if inList[i] > max:
                max = inList[i]
        return max
print(maximum([37,2,1,-9]))

def ultimateAnalysis(inList):
    sum = sumTotal(inList)
    av = avg(inList)
    min = minimum(inList)
    max = maximum(inList)

    retDict = {
       "sumTotal": sum,
       "average": av,
       "minimum": min,
       "maximum": max 
    }
    return retDict
print(ultimateAnalysis([37,2,1,-9]))    

def reverseList(inList):
    
    for i in range(0, int(len(inList) / 2), 1):
        temp = inList[i]
        inList[i] = inList[len(inList) - 1 - i]
        inList[len(inList) - 1 - i] = temp
    return inList

print(reverseList([37,2,1,-9]))