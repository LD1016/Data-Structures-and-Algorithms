class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        # stack = []
        # check = ''
        # for i in A:
        #     if i == '(' or i == '{' or i == '[':
        #         stack.append(i)
        #         continue
        #     if len(stack) > 0:
        #         check = stack.pop()
        #     if i == ')':
        #         if check != '(':
        #             return 0
        #     elif i == '}':
        #         if check != '{':
        #             return 0
        #     elif i == ']':
        #         if check != '[':
        #             return 0
        # if len(stack) == 0:
        #     return 1
        # return 0
        check = {'(': ')', '[': ']', '{': '}'}
        stack = []
        if len(A) == 0 and A[0] not in check.keys():
            return 0
        for i in A:
            if i in check.keys():
                stack.append(i)
            elif len(stack) == 0:
                return 0
            else:
                if i == check[stack[-1]]:
                    stack.pop()
                else:
                    return 0
        if len(stack) == 0:
            return 1
        else:
            return 0


test = Solution()
print(test.isValid("()[]{}"))
