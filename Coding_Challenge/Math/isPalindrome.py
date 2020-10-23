class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A < 0 or A % 10 == 0 and A != 0:
            return 0
        if A == 0:
            return 1
        haft = 0
        temp = A
        i = 0
        while haft < temp:
            haft = haft * (10) + (temp % 10)
            temp = temp // 10
            i += 1
            print(haft, temp, i, A)
        return 1 if haft == temp or haft // 10 == temp else 0


test = Solution()
print(test.isPalindrome(12121))
print(test.isPalindrome(2147447412))
