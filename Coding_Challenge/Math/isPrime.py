class Solution:
    # Because if a number has a factor D, it can be expressed as N = D * (N/D).
    # Now one of D or N/D has to be smaller or equal to Sqrt(N)
    # One factore should be <= sqrt(n) and another should be >= sqrt(n)

    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A == 1:
            return 0
        upperLimit = int(A**0.5)
        for i in range(2, upperLimit + 1):
            if i < A and A % i == 0:
                return 0
        return 1

test = Solution()
print(test.isPrime(3))
print(test.isPrime(6))
