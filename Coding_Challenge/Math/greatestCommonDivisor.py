class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if (A == 0 or B == 0):
            return max(A, B)
        if (A % B == 0 or B % A == 0):
            return min(A, B)
        smaller = min(A, B)
        bigger = max(A, B)
        result = 1
        factorBigger = set()
        for i in range(2, int((smaller**0.5)) + 1):
            if smaller % i == 0:
                factorBigger.add(i)
                factorBigger.add(smaller//i)
        for i in factorBigger:
            if bigger % i == 0:
                result = max(result, i)
        return result


test = Solution()
print(test.gcd(12, 9))
print(test.gcd(3, 9))
