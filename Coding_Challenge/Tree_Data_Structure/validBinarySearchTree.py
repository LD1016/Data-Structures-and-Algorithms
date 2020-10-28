"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
Both the left and right subtrees must also be binary search trees.
Example :

Input : 
   1
  /  \
 2    3

Output : 0 or False


Input : 
  2
 / \
1   3

Output : 1 or True 

"""

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        # def _isValidBSTHelper(A, minVal, maxVal):
        #     if A is None:
        #         return 1
        #     if minVal < A.val < maxVal and _isValidBSTHelper(A.left, minVal, A.val) and _isValidBSTHelper(A.right, A.val, maxVal):
        #         return 1
        #     return 0
        # return _isValidBSTHelper(A, -float('inf'), float('inf'))

        if A is None:
            return 1

        def _isValidBSTHelper(A):
            if A is None:
                return A
            return _isValidBSTHelper(A.left) + [A.val] + _isValidBSTHelper(A.right)
        result = _isValidBSTHelper(
            A.left) + [A.val] + _isValidBSTHelper(A.right)
        curr = result[0]
        for i in range(1, len(result)):
            if result[i] <= curr:
                return 0
            curr = result[i]
        return 1
