"""
Given an integer array A of size N. You need to count the number of special 
elements in the given array. A element is special if removal of that element 
make the array balanced.
Array will be balanced if sum of even index element equal to sum of odd index element.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109

Input Format
First and only argument is an integer array A of size N.

Output Format
Return an integer denoting the count of special elements.

Example Input
Input 1:
 A = [2, 1, 6, 4]
Input 2:
 A = [5, 5, 2, 5, 8]

Example Output
Output 1:
 1
Output 2:
 2

Example Explanation
Explanation 1:
 After deleting 1 from array : {2,6,4}
    (2+4) = (6)
 Hence 1 is the only special element, so count is 1

Explanation 2:
 If we delete A[0] or A[1] , array will be balanced
    (5+5) = (2+8)
 So A[0] and A[1] are special elements, so count is 2.
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # result = 0
        # if len(A) <= 1:
        #     return len(A)
        # if len(A) == 2:
        #     return 1 if A[0] == A[1] else 0
        # for i in range(len(A)):
        #     prefixOddSum = self.sumOdd(True, A[:i])
        #     prefixEvenSum  = self.sumOdd(False, A[:i])
        #     suffixOddSum = self.sumOdd(True, [0] + A[i+1:])
        #     suffixEvenSum  = self.sumOdd(False, [0] + A[i+1:])
        #     print('prefixOddSum + suffixOddSum: ', prefixOddSum + suffixOddSum)
        #     print('prefixEvenSum + suffixEvenSum: ', prefixEvenSum + suffixEvenSum)
        #     result = result + 1 if prefixOddSum + suffixOddSum == prefixEvenSum + suffixEvenSum else result
        # return result
        x = y = x1 = y1 = 0
        for i in range(len(A)):
            if i % 2 == 0:
                x += A[i]
            else:
                y += A[i]
        result = 0
        for i in range(len(A)):
            if i % 2 == 0:
                x -= A[i]
                if x + y1 == y + x1:
                    result += 1
                x1 += A[i]
            else:
                y -= A[i]
                if x + y1 == y + x1:
                    result += 1
                y1 += A[i]
        return result

    def sumOdd(self, ifOdd, A):
        result = 0
        for i in range(len(A)):
            if ifOdd:
                result = result + A[i] if i % 2 == 0 else result
            else:
                result = result + A[i] if i % 2 != 0 else result
        return result


test = Solution()
print(test.solve([2, 1, 6, 4]))
