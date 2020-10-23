class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if A <= 1:
            return A
        remainder = 0
        quotient = A
        result = []
        while quotient > 1:
            quotient, remainder = quotient//2, quotient%2
            if remainder !=  0:
                result.insert(0, 1)
            else:
                result.insert(0, 0)
        result.insert(0, 1)
        strings = [str(integer) for integer in result]
        a_string = "". join(strings)
        an_integer = int(a_string)
        return an_integer

test = Solution()

print(test.findDigitsInBinary(6))
print(test.findDigitsInBinary(12))