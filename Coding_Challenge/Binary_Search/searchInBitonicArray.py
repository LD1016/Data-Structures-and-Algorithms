class Solution:
    def solve(self, A, B):
        highest = self.findHighest(A)
        if A[highest] == B:
            return highest
        firstHaft = self.binarySearch(A[:highest], B)
        secondHaft = self.binarySearch(A[highest+1:], B)
        if firstHaft != -1:
            return firstHaft
        if secondHaft != -1:
            return highest + secondHaft + 1
        return -1

    def findHighest(self, A):
        s, e, m = 0, len(A)-1, 0
        while s <= e:
            m = (s+e)//2
            if A[m-1] < A[m] < A[m+1]:
                s = m + 1
            elif A[m-1] > A[m] > A[m+1]:
                e = m - 1
            else:
                break
        return m

    def binarySearch(self, A, B):
        s, e = 0, len(A) - 1
        while s <= e:
            m = (s+e)//2
            if A[m] == B:
                return m
            if A[m] < B:
                s = m+1
            elif A[m] > B:
                e = m-1
        return -1


test = Solution()
print(test.solve([3, 9, 10, 20, 17, 5, 1], 10))
print(test.solve([5, 6, 7, 8, 9, 10, 3, 2, 1], 30))
print(test.solve([5, 6, 7, 8, 9, 10, 3, 2, 1], 2))
print(test.solve([5, 6, 7, 8, 9, 10, 3, 2, 1], 8))
