"""
767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters 
that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
 
"""

import heapq


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        time: nlog(n)
        space: n
        """
        hashMap = {}
        for i in S:
            if i in hashMap.keys():
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        heap, ans = [], ""
        for k, v in hashMap.items():
            heapq.heappush(heap, (-v, k))
        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            ans += char1 + char2
            if count1 + 1 < 0:
                heapq.heappush(heap, (count1+1, char1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2+1, char2))
        if heap:
            count1, char1 = heapq.heappop(heap)
            if count1 + 1 < 0:
                return ''
            ans += char1
        return ans


if __name__ == "__main__":
    test = Solution()
    print(test.reorganizeString('aab'))
    print(test.reorganizeString('aaab'))
