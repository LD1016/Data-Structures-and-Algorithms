def findFactorialRecursive(n):
    if n == 1:
        return 1 
    return n * findFactorialRecursive(n-1)

print(findFactorialRecursive(5))
print(findFactorialRecursive(4))
print(findFactorialRecursive(3))
