#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        self.backtracking(nums,res,[],0)
        return res
    
    def backtracking(self,nums,res,list,index):
        res.append(list)
        for i in range(index,len(nums)):
            self.backtracking(nums,res,list+[nums[i]],i+1)
# @lc code=end

