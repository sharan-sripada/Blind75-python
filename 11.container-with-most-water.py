#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <2: return 0
        i,j = 0, len(height)-1
        area=0
        while i<j:
            area=max(area, min(height[i], height[j])*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area
        
# @lc code=end

