def countdown(num):
    retList = []

    for i in range(num + 1, -1, -1):
        retList.append(i)
    return retList

print(countdown(5))