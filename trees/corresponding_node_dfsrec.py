# leetcode: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    def getTargetCopy(self, original, cloned, target):
        def inorder(original, cloned):
            if original.left:
                inorder(original.left, cloned.left)
            if original == target:
                self.ans = cloned
            if original.right:
                inorder(original.right, cloned.right)

        inorder(original, cloned)
        return self.ans