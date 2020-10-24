def binarySearch(A, target):
    start, end = 0, len(A)-1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


print(binarySearch([1, 8, 21, 32, 45], 45))
print(binarySearch([1, 8, 21, 32, 45], 21))
print(binarySearch([1, 8, 21, 32, 45], 8))
