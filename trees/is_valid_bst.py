# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        if not root:
            return True

        st = [(root, -float('inf'), float('inf'))]

        while st:
            node, low, high = st.pop()
            
            if not node:
                continue
            if not (node.val > low and node.val < high):
                return False
            
            st.append((node.left, low, node.val))
            st.append((node.right, node.val, high))
        return True