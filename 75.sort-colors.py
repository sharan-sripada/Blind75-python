#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        k=len(nums)-1
        while j<=k:
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[j]==2:
                nums[k],nums[j]=nums[j],nums[k]
                k-=1
            else:
                j+=1
        
# @lc code=end

