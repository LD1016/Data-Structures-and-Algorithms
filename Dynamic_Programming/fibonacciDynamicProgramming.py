def fibonacciDP(n): 
    cach = {}
    def helper(n):
        if n < 2:
            return n 
        if n in cach.keys():
            return cach[n]
        cach[n] = helper(n-1) + helper(n-2)
        return cach[n]
    return helper(n)

print(fibonacciDP(7))
print(fibonacciDP(10))