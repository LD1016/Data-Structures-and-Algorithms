def rotatedArray(A):
    start, end = 0, len(A)-1
    while start <= end:
        if A[start] <= A[end]:
            return start
        mid = (start + end) // 2
        prev, next = (mid - 1 + len(A)) % len(A), (mid+1) % len(A)
        if A[mid] <= A[prev] and A[mid] <= A[next]:
            return mid
        if A[start] <= A[mid]:
            start = mid + 1
        elif A[mid] <= A[end]:
            end = mid - 1
    return -1


print(rotatedArray([15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]))
