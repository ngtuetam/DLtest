# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = self.cur = TreeNode()
        cur_node = root
        st = []
        while cur_node or st:
            while cur_node:
                st.append(cur_node)
                cur_node = cur_node.left
            cur_node = st.pop()
            self.cur.right = TreeNode(cur_node.val)
            self.cur = self.cur.right
            cur_node = cur_node.right
        return ans.right