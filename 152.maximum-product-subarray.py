#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p,n = nums[0],nums[0]
        prd = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                p,n=n,p
            p=max(nums[i],nums[i]*p)
            n=min(nums[i],nums[i]*n)
            prd=max(prd,max)
        return prd
            
            
            
            
            
            
            
        
        
# @lc code=end

