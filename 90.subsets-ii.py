#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        self.backtracking(nums,res,[],0)
        return res
    
    def backtracking(self,nums,res,list,index):
        res.append(list)
        for i in range(index,len(nums)):
            if i> index and nums[i]==nums[i-1]:
                continue
            self.backtracking(nums,res,list+[nums[i]],i+1)
        
# @lc code=end

