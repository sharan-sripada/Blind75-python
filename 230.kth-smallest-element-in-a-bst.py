#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=None
        self.count=k
        self.helper(root)
        return self.ans
    def helper(self,root):
        if not root:
            return
        self.helper(root.left)
        self.count-=1
        if self.count==0:
            self.ans=root.val
            return
        self.helper(root.right)
        
        
# @lc code=end

