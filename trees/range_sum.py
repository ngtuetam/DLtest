# leetcode: Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        st = [root]
        ans = 0
        while st:
            node = st.pop()
            if node:
                if low <= node.val <= high:
                    ans+= node.val
                if node.val > low:
                    st.append(node.left)
                if node.val < high:
                    st.append(node.right)
        return ans
