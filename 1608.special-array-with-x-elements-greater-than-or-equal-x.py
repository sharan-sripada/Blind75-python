#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        i,j=0,len(nums)-1
        ans=-1
        while(j>=0):
            if n-j <= nums[j] and j-1 >=0 and n-j > nums[j-1]:
                ans=max(n-j,ans)
            
            j=j-1
        if n<=nums[0]:
            return n
            
        return ans
        
        
        
        
        
# @lc code=end

