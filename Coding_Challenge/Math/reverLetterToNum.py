class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        letterIndex = {k: v+1 for v, k in enumerate(letters)}
        # T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
        A = list(A)
        A = A[::-1]
        result = 0
        i = 0
        while i < len(A):
            result += (26**i * letterIndex[A[i]])
            i += 1
        return result


test = Solution()
print(test.titleToNumber('AB'))
print(test.titleToNumber('AAA'))
print(test.titleToNumber('B'))
