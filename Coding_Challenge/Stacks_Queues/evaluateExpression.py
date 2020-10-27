class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        # numStack = []
        # for symb in A:
        #     numStack.append(int(eval("{2}{1}{0}".format(
        #         numStack.pop(), symb, numStack.pop())) if symb in "+-*/" else symb))
        # return numStack[0]
        D = dict(zip("+-*/", ['add', 'sub', 'mul', 'floordiv']))
        S = []
        for i in A:
            if i in D:
                x, y = S.pop(), S.pop()
                if D[i] == 'add':
                    S.append(y + x)
                elif D[i] == 'sub':
                    S.append(y - x)
                elif D[i] == 'mul':
                    S.append(y * x)
                elif D[i] == 'floordiv':
                    S.append(y // x)
            else:
                S.append(int(i))
        return S[0]


test = Solution()
print(test.evalRPN(["2", "1", "+", "3", "*"]))
print(test.evalRPN(["4", "13", "5", "/", "+"]))
