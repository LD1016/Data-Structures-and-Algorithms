class Solution:
    # @param A : list of integers
    # @return an integer

    def maxSpecialProduct(self, A):
        import sys
        if len(A) <= 3:
            return 0
        result = -sys.maxsize - 1
        for i in range(1, len(A) - 1):
            # print(i)
            leftSp = self.leftSp(A[:i], 0, i, A[i])
            # print(A[:i])
            rightSp = self.rightSp(A[i+1:], i, len(A)-1, A[i])
            # print(A[i+1:])
            result = max(result, leftSp * rightSp)
        return result

    def leftSp(self, A, start, end, target):
        result = 0
        while A:
            temp = A.pop()
            if temp > target:
                result = max(result, len(A))
        return result

    def rightSp(self, A, start, end, target):
        result = end
        i = 0
        while A:
            temp = A[0]
            del A[0]
            if temp > target:
                result = min(result, start + 1 + i)
            i += 1
        return result


test = Solution()
print(test.maxSpecialProduct([1, 4, 3, 4]))
print(test.maxSpecialProduct([10, 7, 100]))
print(test.maxSpecialProduct([5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]))
print(test.maxSpecialProduct([7, 5, 7, 9, 8, 7]))
