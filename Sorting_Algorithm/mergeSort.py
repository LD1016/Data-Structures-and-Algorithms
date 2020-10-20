def merge(left, right):
    result = []
    leftIndex = 0 
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] > right[rightIndex]:
            result.append(right[rightIndex])
            rightIndex += 1
        else: 
            result.append(left[leftIndex])
            leftIndex += 1
    return result + left[leftIndex:] + right[rightIndex:]

def mergeSort(arr):
    if (len(arr) == 1):
        return arr
    haft = len(arr) // 2 
    left = arr[:haft]
    right = arr[haft:]
    return merge(mergeSort(left), mergeSort(right))

    
print(mergeSort([1, 5, 9, 2, 3]))