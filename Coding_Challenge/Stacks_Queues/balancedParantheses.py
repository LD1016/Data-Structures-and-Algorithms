class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) < 1 or A[0] == ')':
            return 0
        stack = []
        for i in A:
            if i == '(':
                stack.append(')')
            else:
                if len(stack) == 0:
                    return 0
                stack.pop()
        return 0 if len(stack) != 0 else 1


test = Solution()
print(test.solve("(()())"))
print(test.solve("(()"))
