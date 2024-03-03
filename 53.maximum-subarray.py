#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r,sum,maxSum=0,0,0,-inf
        while(r<len(nums)):

            sum+=nums[r]
            maxSum=max(sum,maxSum)
            if(sum<=0):
                l=r
                sum=0
            r+=1
        return maxSum
        
        


        
# @lc code=end

