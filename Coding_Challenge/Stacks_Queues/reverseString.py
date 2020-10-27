class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        result = ''
        # for i in reversed(range(len(A))):
        for i in range(len(A)-1, -1, -1):
            result += A[i]
        return result


test = Solution()
print(test.reverseString('abc'))
print(test.reverseString('Hello World!'))
