array = [8,3,5,7,0,2,1]

def insertionSort(arr):
    for i in range(1,len(arr)):
        compVal = arr[i]

        j = i - 1
        while j >= 0 and compVal < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = compVal
    return arr    

print(insertionSort(array))        