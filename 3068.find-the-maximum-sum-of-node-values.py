#
# @lc app=leetcode id=3068 lang=python3
#
# [3068] Find the Maximum Sum of Node Values
#

# @lc code=start
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(n^k)-n for n in nums]
        delta.sort(reverse=True)
        
        maxValue = sum(nums)
        
        for i in range(0,len(nums)-1,2):
            if delta[i] + delta[i+1] > 0:
                maxValue = maxValue + delta[i] + delta[i+1]
            
        return maxValue
# @lc code=end

