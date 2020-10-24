def bubbleSort(arr):
    for i in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


print(bubbleSort([1, 5, 9, 2, 3]))
