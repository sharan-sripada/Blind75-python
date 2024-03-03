#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        nums.sort(reverse=True)
        if s%2 ==1:
            return False
        s=s//2

        self.dp.clear()
        return self.helper(nums,0,s,0)

    dp ={}
    
    def helper(self,nums,i,sum,ans):
        if (i,sum) in self.dp:
            return self.dp[(i,sum)]
        if sum < ans:
            return False
        if i>=len(nums):
            return False
        if sum == nums[i]:
            return True
        self.dp[(i,sum)]=self.helper(nums,i+1,sum,ans) or self.helper(nums,i+1,sum-nums[i],ans)
        
        return self.dp[(i,sum)]
        
        
# @lc code=end

