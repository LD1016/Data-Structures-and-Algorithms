"""
Given a number N, find all factors of N.

Example:
N = 6 
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.
"""


class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        firstHaft = []
        secondHaft = []
        if A == 1:
            return [A]
        for i in range(1, int(A**0.5)+1):
            if A % i == 0:
                firstHaft.append(i)
                secondHaft.insert(0, A//i)
        return firstHaft + secondHaft if firstHaft[-1] != secondHaft[0] else firstHaft + secondHaft[1:]


test = Solution()
print(test.allFactors(6))
print(test.allFactors(85463))
