#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter =0 

        def depth(p):
            nonlocal maxDiameter 
            if p == None:
                return 0
            right = depth(p.right)
            left = depth(p.left)
            maxDiameter = max(maxDiameter, right+left)
            return 1 + max(left,right)
        
        depth(root)
        return maxDiameter
        
# @lc code=end

