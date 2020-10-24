class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        index = self.binarySearch(A, B)
        if index == -1:
            return 0
        result = 0
        for i in reversed(range(index)):
            if A[i] == B:
                result += 1
            else:
                break
        for i in range(index, len(A)):
            if A[i] == B:
                result += 1
            else:
                break
        return result

    def binarySearch(self, A, T):
        start, end = 0, len(A)-1
        while start <= end:
            mid = (start + end) // 2
            if A[mid] == T:
                return mid
            elif A[mid] < T:
                start = mid + 1
            else:
                end = mid - 1
        return -1


test = Solution()
print(test.findCount([5, 7, 7, 8, 8, 10], 8))
print(test.findCount([5, 7, 8, 8, 8, 10], 8))
print(test.findCount([8, 8, 8, 8, 8, 8, 8], 8))
