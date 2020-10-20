def findFactorialIterative(n):
    result = 1 
    while n > 0: 
        result *= n 
        n -= 1 
    return result

print(findFactorialIterative(5))
print(findFactorialIterative(4))
print(findFactorialIterative(3))