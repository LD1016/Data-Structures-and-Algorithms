def fibonacciDP(n):
    cache = {}

    def helper(n):
        if n < 2:
            return n
        if n in cache.keys():
            return cache[n]
        cache[n] = helper(n-1) + helper(n-2)
        return cache[n]
    return helper(n)


print(fibonacciDP(7))
print(fibonacciDP(10))
