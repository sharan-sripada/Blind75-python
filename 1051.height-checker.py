#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorteed(heights)
        ans=0
        for i in range(len(nums)):
            if heights[i]!=expected[i]:
                ans+=1
        return ans
        
# @lc code=end

