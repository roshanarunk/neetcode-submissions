# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(root):
            nonlocal longest
            if root == None:
                return 0
            left = dfs(root.left)
            if root.left:
                left += 1
            right = dfs(root.right)
            if root.right:
                right += 1
            longest = max(longest, left + right)
            return max(left, right)
        return max(dfs(root), longest)