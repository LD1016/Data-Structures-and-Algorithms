class Solution:
    # @param A : list of integers
    # @return an integer
    def perfectPeak(self, A):
        # sortOfA = A[:]
        # sortOfA.sort()
        # for i in range(1,len(A)-1):
        #     if A[i] == sortOfA[i]:
        #         print(A[i])
        #         return True 
        # return False
        # for i in range(1, len(A)-1):
        #     leftArr, rightArr = A[:i], A[i+1:]
        #     maxLeft = max(leftArr)
        #     minRight = min(rightArr)
        #     if maxLeft < A[i] < minRight:
        #         return True
        # return False
        right_min = [0] * len(A)
        left_max = [0] * len(A)
        right_min[-1] = 1
        left_max[0] = 1
        minVal = A[-1]
        maxVal = A[0]
        for i in reversed(range(len(A)-1)):
            if A[i] < minVal:
                right_min[i] = 1
                minVal = A[i]
        for i in range(len(A)-1):
            if A[i] > maxVal:
                left_max[i] = 1
                maxVal = A[i]
        for a, b in zip(right_min[1:], left_max[1:]):
            if a == b == 1:
                return True
        return False
            

    
test = Solution()
print(test.perfectPeak([5, 1, 4, 3, 6, 8, 10, 7, 9]))
print(test.perfectPeak([ 24649, 2422, 18936, 14894, 17808, 17452, 22484, 3729, 3789, 27939, 6901, 468, 16520, 14310, 5250, 18128, 14311, 31557, 26419, 7617, 20601, 22814, 6618, 9515 ]))