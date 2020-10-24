class Solution:
    def pow(self, x, n, d):
        cache = {}

        def helper(x, n, d):
            if n == 0:
                return 1 if x else 0
            if n == 1:
                return x % d
            if n in cache.keys():
                return cache[n]
            cache[n] = (helper(x, n//2, d) * helper(x, n//2, d)) % d
            if n % 2 == 1:
                cache[n] = (cache[n] * x) % d
            return cache[n]
        return helper(x, n, d)


test = Solution()
print(test.pow(2, 3, 3))
