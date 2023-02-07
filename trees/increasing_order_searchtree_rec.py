# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.cur = TreeNode()
        def inorder(node):
            if node:
                inorder(node.left)

                self.cur.right = TreeNode(node.val)
                self.cur = self.cur.right

                inorder(node.right)

        inorder(root)
        return ans.right