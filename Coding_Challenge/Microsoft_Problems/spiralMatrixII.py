"""
Spiral Matrix II

Given a positive integer n, generate an n x n matrix filled with elements 
from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 
Constraints:

1 <= n <= 20
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return [[]]
        result = [[0 for i in range(n)] for j in range(n)]
        right, left, top, bottom = n-1, 0, 0, n-1
        number = 0
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                number += 1
                result[top][i] = number
            top += 1
            for i in range(top, bottom+1):
                number += 1
                result[i][right] = number
            right -= 1
            for i in range(right, left-1, -1):
                number += 1
                result[bottom][i] = number
            bottom -= 1
            for i in range(bottom, top-1, -1):
                number += 1
                result[i][left] = number
            left += 1
        return result


test = Solution()
print(test.generateMatrix(3))
print(test.generateMatrix(4))
