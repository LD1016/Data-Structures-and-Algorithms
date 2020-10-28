"""
Given a BST node, return the node which has value just greater than the given node.

Example:

Given the tree

               100
              /   \
            98    102
           /  \
         96    99
          \
           97
Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
If there are no successor in the tree ( the value is the largest in the tree, return NULL).

Using recursion is not allowed.

Assume that the value is always present in the tree.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        # def _getSuccessorHelper(A):
        #     if A is None:
        #         return []
        #     return _getSuccessorHelper(A.left) + [A] + _getSuccessorHelper(A.right)
        # arr = _getSuccessorHelper(A.left) + [A] + _getSuccessorHelper(A.right)
        # lastNode = arr[-1]
        # if B == lastNode.val:
        #     return None
        # for i in range(len(arr)):
        #     node = arr[i]
        #     if B == node.val:
        #
        root = A
        successor = root
        while root.val != B:
            if root.val > B:
                successor = root
                root = root.left
            else:
                root = root.right
        if root.right != None:
            root = root.right
            while root.left != None:
                root = root.left
            return root
        else:
            if successor.val <= B:
                return None
            return successor
