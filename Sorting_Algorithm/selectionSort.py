import sys
def selectionSort(arr):
    smallest = sys.maxsize
    indexSmallest = 0
    for i in range(len(arr)):
        smallest = arr[i]
        indexSmallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < smallest: 
                indexSmallest = j 
                smallest = arr[j]
        arr[i], arr[indexSmallest] =  arr[indexSmallest], arr[i]
    return arr 

print(selectionSort([1, 5, 9, 2, 3]))