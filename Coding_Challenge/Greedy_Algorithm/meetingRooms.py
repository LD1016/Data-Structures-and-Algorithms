"""
Given an 2D integer array A of size N x 2 denoting time intervals of different meetings.

Where:

A[i][0] = start time of the ith meeting.
A[i][1] = end time of the ith meeting.
Find the minimum number of conference rooms required so that all meetings can be done.

Example Input
Input 1:
 A = [      [0, 30]
            [5, 10]
            [15, 20]
     ]

Input 2:
 A =  [     [1, 18]
            [18, 23]
            [15, 29]
            [4, 15]
            [2, 11]
            [5, 13]
      ]

Example Output
Output 1:
 2
Output 2:
 4
"""

from collections import defaultdict


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        d = defaultdict(lambda: 0)
        for a, b in A:
            d[a] += 1
            d[b] -= 1

        ans = 0
        cnt = 0
        times = sorted(list(d.keys()))
        for t in times:
            # print(t, d[t])
            cnt += d[t]
            ans = max([ans, cnt])

        return ans


test = Solution()
print(test.solve([[0, 30],
                  [5, 10],
                  [15, 20]
                  ]))
print(test.solve([[1, 18],
                  [18, 23],
                  [15, 29],
                  [4, 15],
                  [2, 11],
                  [5, 13]
                  ]))
