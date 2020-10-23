class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        # if A == 1:
        #     return [A]
        # result = []
        # for i in range(1, A // 2 + 1):
        #     if A % i == 0:
        #         result.append(i)
        # result.append(A)
        # return result
        if A == 1:
            return [A]
        result = set() 
        for i in range(1, int(A**0.5) + 1):
            if A % i == 0 and i not in result:
                result.add(i)
                result.add(A//i)
        result = list(result)
        result.sort()
        return result
                

test = Solution()
print(test.allFactors(6))
print(test.allFactors(85463))