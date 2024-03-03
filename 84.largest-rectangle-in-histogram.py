#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        maxA = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                maxA = max(maxA, h * w)
            stack.append(i)
        heights.pop()
        return maxA
                
        
# @lc code=end

