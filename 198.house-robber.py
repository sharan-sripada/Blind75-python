#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l<=2:
            return max(nums)
        ans=[0,nums[0]]
        
        for i in range(1,l,1):
            ans.append(max(ans[i-1]+nums[i],ans[i]))       
        return ans[l]
        
# @lc code=end

