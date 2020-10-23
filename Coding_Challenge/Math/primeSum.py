class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        for i in range(2, (A//2) + 1):
            if self.isPrime(i) and self.isPrime(A-i):
                return [i, A-i]
        return []

    def isPrime(self, A):
        if A <= 1: 
            return False 
        upperLimit = int(A**0.5) + 1
        for i in range(2, upperLimit):
            if A % i == 0:
                return False 
        return True

test = Solution()
print(test.primesum(16777214))