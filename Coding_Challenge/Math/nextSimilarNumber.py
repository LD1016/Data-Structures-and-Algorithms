def nextSimilarNumber(A):
    l = len(A)
    idx = l-2
    while(idx >= 0):
        if(A[idx] < A[idx+1]):
            j = l-1
            while(A[j] <= A[idx]):
                j -= 1
            A = A[:idx]+A[j]+A[l-1:j:-1]+A[idx]+A[j-1:idx:-1]
            return(A)
        idx -= 1
    return('-1')


print(nextSimilarNumber('218765'))
# print(nextSimilarNumber('4321'))
