def fibonacciRecursive(n):
    if n == 0 or n == 1:
        return n 
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

print(fibonacciRecursive(8))
print(fibonacciRecursive(3))