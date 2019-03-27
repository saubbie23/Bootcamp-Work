def retPrime(num):
    for i in range(2, num//2, 1):
        if num % i == 0:
            return True
    return False

#print(retPrime(5))

def addArray(arr, val):
    arr.append(val)

    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i-1]
        print(arr)
    arr[0] = val
    return arr

print(addArray([1,2,3],4))