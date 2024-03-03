#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, list):
        if len(nums) == len(list):
            res.append(list)
            return
        for i in range(0,len(nums)):
            if nums[i] in list:
                continue
            self.dfs(nums,res,list+[nums[i]])
# @lc code=end

