#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited= [False]* len(nums)
        nums.sort()
        self.dfs(nums, res, [],visited)
        return res
    
    def dfs(self, nums, res, list, visited):
        if len(nums) == len(list):
            res.append(list)
            return
        for i in range(0,len(nums)):
            if visited[i]==True:
                continue
            if i>0 and nums[i-1]==nums[i] and visited[i-1]== False:
                continue
            visited[i] = True
            self.dfs(nums,res,list+[nums[i]],visited)
            visited[i] = False
        
# @lc code=end

