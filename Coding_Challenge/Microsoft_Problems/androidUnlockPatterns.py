"""
Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" by connecting the dots in a specific sequence, forming a series of joined line segments where each segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock pattern if both of the following are true:

All the dots in the sequence are distinct.
If the line segment connecting two consecutive dots in the sequence passes through any other dot, the other dot must have previously appeared in the sequence. No jumps through non-selected dots are allowed.
Here are some example valid and invalid unlock patterns:


The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but dot 2 did not previously appear in the sequence.
The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but dot 5 did not previously appear in the sequence.
The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 meets the condition because dot 2 previously appeared in the sequence.
The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 9 meets the condition because dot 5 previously appeared in the sequence.
Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid lock screen that consist of at least m keys and at most n keys.

Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, or the order of the dots is different.

Time complexity: K * n!
Space complexity: n
"""


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def dfs(vis, cur, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            res = 0
            vis.add(cur)
            for i in range(1, 10):
                if i not in vis and ((cur, i) not in skip or skip[(cur, i)] in vis):
                    res += dfs(vis, i, remain-1)
            vis.remove(cur)
            return res

        skip = {(1, 3): 2, (1, 7): 4, (3, 9): 6, (7, 9): 8, (1, 9): 5, (2, 8): 5, (3, 7): 5, (4, 6): 5,
                (3, 1): 2, (7, 1): 4, (9, 3): 6, (9, 7): 8, (9, 1): 5, (8, 2): 5, (7, 3): 5, (6, 4): 5}
        ans, vis = 0, set()
        for i in range(m, n+1):
            ans += dfs(vis, 1, i-1) * 4
            ans += dfs(vis, 2, i-1) * 4
            ans += dfs(vis, 5, i-1)
        return ans


test = Solution()
print(test.numberOfPatterns(1, 2))
