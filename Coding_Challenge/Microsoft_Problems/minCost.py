"""
1578. Minimum Deletion Cost to Avoid Repeating Letters

Given a string s and an array of integers cost where cost[i] is the cost of 
deleting the ith character in s.
Return the minimum cost of deletions such that there are no two identical 
letters next to each other.

Notice that you will delete the chosen characters at the same time, 
in other words, after deleting a character, the costs of deleting 
other characters will not change.


Example 1:
Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:
Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:
Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
 

Constraints:

s.length == cost.length
1 <= s.length, cost.length <= 10^5
1 <= cost[i] <= 10^4
s contains only lowercase English letters.
"""


class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        ans = 0
        total = 0
        maxGroup = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                ans += total - maxGroup
                total = 0
                maxGroup = 0
            total += cost[i]
            maxGroup = max(maxGroup, cost[i])
        ans += total - maxGroup
        return ans


if __name__ == "__main__":
    test = Solution()
    print(test.minCost("abaac", [1, 2, 3, 4, 5]))
    print(test.minCost("abc", [1, 2, 3]))
    print(test.minCost("aabaa", [1, 2, 3, 4, 1]))
