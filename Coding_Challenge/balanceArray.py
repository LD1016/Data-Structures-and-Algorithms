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