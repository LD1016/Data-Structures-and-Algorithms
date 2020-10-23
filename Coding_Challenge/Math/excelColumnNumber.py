class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        if A == 1:
            return 'A'
        letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        letterIndex = {k+1: v for k, v in enumerate(letters)}
        if A <= 26:
            return letterIndex[A]
        result = []
        quotient = A
        remainder = 0
        while quotient > 1:
            quotient, remainder = quotient // 26, quotient % 26
            result.insert(0, letterIndex[remainder])
        result.insert(0, 'A')
        result = "".join(result)
        return result


test = Solution()
print(test.titleToNumber(28))
print(test.titleToNumber(27))
print(test.titleToNumber(26))
