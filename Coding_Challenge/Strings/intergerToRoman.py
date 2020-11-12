"""
Input 1:
    A = 5
Output 1:
    "V"

Input 2:
    A = 14
Output 2:
    "XIV"

"""


class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        dictRoNum = {1: 'I', 5: 'V', 10: 'X',
                     50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        i = 0
        result = ''
        while A != 0:
            last, A = A % 10, A//10
            if last == 0:
                i += 1
                continue
            key = 10**i
            if key*last in dictRoNum.keys():
                result = dictRoNum[key*last] + result
            elif (last+1)*key in dictRoNum.keys():
                result = dictRoNum[key] + dictRoNum[(last+1)*key] + result
            else:
                while last != 0 and last != 5:
                    result = dictRoNum[key] + result
                    last -= 1
                if last == 5:
                    result = dictRoNum[last*key] + result
            i += 1
        return result


test = Solution()
print(test.intToRoman(10))
print(test.intToRoman(59))
print(test.intToRoman(2475))
