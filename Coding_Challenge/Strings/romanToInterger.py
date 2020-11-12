"""
Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

For Example
Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20

Input 3:
    A = "MMCDLXXV"
Output 2:
    2475

"""


class Solution:
    # @param A : string
    # @return an integer
    # I, V, X, L, C, D, and M --> 1, 5, 10, 50, 100, 500, and 1,000
    def romanToInt(self, A):
        dictRoNum = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        i, n = 0, len(A)
        while i < n:
            if i+1 < n and dictRoNum[A[i]] < dictRoNum[A[i+1]]:
                result = result + dictRoNum[A[i+1]] - dictRoNum[A[i]]
                i += 1
            else:
                result = result + dictRoNum[A[i]]
            i += 1
        return result


test = Solution()
print(test.romanToInt("MMCDLXXV"))
print(test.romanToInt("XIV"))
print(test.romanToInt("XX"))
