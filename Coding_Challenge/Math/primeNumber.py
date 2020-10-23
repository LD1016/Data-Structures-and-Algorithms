class Solution:
    def primeNumber(self, A):
        if A <= 1:
            return []
        nonePrimes = set()
        primes = []
        x = 2 
        while x <= A:
            if x not in nonePrimes:
                primes.append(x)
            for i in range(x, A+1, x):
                nonePrimes.add(i)
            x += 1
        return primes


test = Solution()
print(test.primeNumber(100000))