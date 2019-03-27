array = [8,3,5,7,0,2,1]

def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]        
        for j in range(i, len(arr), 1):
            if arr[j] < min:
                min = arr[j]
                idx = j
        arr[i], arr[idx] = min, arr[i]
    return arr

print(selectionSort(array))