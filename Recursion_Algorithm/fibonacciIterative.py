def fibonacciIterative(n):
    result = 0
    a = 0
    b = 1 
    while n > 1:
        result = a + b 
        a, b = b, result
        n -= 1
    return result 

print(fibonacciIterative(8))
print(fibonacciIterative(3))