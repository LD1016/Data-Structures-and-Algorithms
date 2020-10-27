class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        # result = 0
        # A = A.strip()
        # for i in range(len(A) - 1, -1, -1):
        #     if A[i] == ' ':
        #         result = len(A) - i - 1
        #         break
        # return len(A) if result == 0 else result
        l = A.split()
        print(l)
        if(len(l) == 0):
            return 0
        return len(l[len(l)-1])


test = Solution()
print(test.lengthOfLastWord("  xDGBklKecz IAcOJYOH O  WY WPi"))
print(test.lengthOfLastWord("Hello World"))
