"""
Minimum number of flips to make binary string alternate

Input : str = “001”
Output : 1
Minimum number of flips required = 1
We can flip 1st bit from 0 to 1 

Input : str = “0001010111”
Output : 2
Minimum number of flips required = 2
We can flip 2nd bit from 0 to 1 and 9th 
bit from 1 to 0 to make alternate 
string “0101010101”.
"""


def flip(A):
    return min(helper(A, '0'), helper(A, '1'))


def helper(A, zeroOrOne):
    count = 0
    for i in range(len(A)):
        if i % 2 == 0 and A[i] != zeroOrOne:
            count += 1
        elif i % 2 != 0 and A[i] == zeroOrOne:
            count += 1
    return count


print(flip('001'))
print(flip('0001010111'))
