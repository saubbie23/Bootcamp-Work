#arr = [1,5,3,2,0,8]
arr = [1,4,7,9,0,8,6]

def bubbleSort(arr):
    sortCount = 1

    while sortCount != 0:
        sortCount = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sortCount += 1

    return arr

print(bubbleSort(arr))