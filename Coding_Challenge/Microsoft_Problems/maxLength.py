"""
Maximum Length of a Concatenated String with Unique Characters

Given an array of strings arr. String s is a concatenation of 
a sub-sequence of arr which have unique characters.
Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.


"""


class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        result = [0]
        self.helper(arr, 0, '', result)
        return result[0]

    def helper(self, arr, index, s, result):
        # count = self.uniqueChars(s)
        # if index == len(arr) and count > result[0]:
        #     result[0] = count
        if index == len(arr) and len(s) == len(set(s)) and len(s) > result[0]:
            result[0] = len(s)
            return
        if index == len(arr):
            return
        self.helper(arr, index+1, s, result)
        self.helper(arr, index+1, s+arr[index], result)

    def uniqueChars(self, s):
        hashMap = {}
        for i in s:
            if i in hashMap.keys():
                return -1
            else:
                hashMap[i] = True
        return len(s)


test = Solution()
print(test.maxLength(["un", "iq", "ue"]))
print(test.maxLength(["cha", "r", "act", "ers"]))
print(test.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
