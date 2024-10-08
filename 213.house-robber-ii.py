#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def justRob(i,j):
            f,s=0,nums[i]
            i+=1
            while i<j:
                val = max(f+nums[i],s)
                f,s=s,val
                i+=1
            return s
        if len(nums)<2:
            return max(nums)
        return max(justRob(0,len(nums)-1),justRob(1,len(nums)))
            
        
        
# @lc code=end

