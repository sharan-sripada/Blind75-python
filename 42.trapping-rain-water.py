#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        res=0
        l,r=[0]*n,[0]*n
        for i in range(1,n):
            l[i]=max(l[i-1],height[i-1])
        for i in range(n-2,0,-1):
            r[i]=max(r[i+1],height[i+1])
            res+= 0 if min(l[i],r[i])<=height[i] else min(r[i],l[i])-height[i]
        return res
# @lc code=end

