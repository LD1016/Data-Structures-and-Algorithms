"""
Check if a given array can represent Preorder Traversal of Binary Search Tree

Input:  pre[] = {40, 30, 35, 80, 100}
Output: true
Given array can represent preorder traversal
of below tree
     40
   /   \
 30    80 
  \      \
  35     100 


Input:  pre[] = {40, 30, 35, 20, 80, 100}
Output: false
Given array cannot represent preorder traversal
of a Binary Search Tree.
"""


def solve(self, A):
    root = -float('inf')
    stack = []
    for val in A:
        if val < root:
            return 0
        while len(stack) != 0 and stack[-1] < val:
            root = stack.pop()
        stack.append(val)
    return 1
