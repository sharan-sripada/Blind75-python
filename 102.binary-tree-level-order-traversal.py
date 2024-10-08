#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        level=[root]
        while root and level:
            ans.append([node.val for node in level ])
            lr=[(node.left,node.right) for node in level]
            level=[node for nodeset in lr for node in nodeset if node]
        return ans
        
# @lc code=end

