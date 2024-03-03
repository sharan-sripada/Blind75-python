#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(range(1,n+1), k, 0, [], res)
        return res
    
    def dfs(self, nums, k, index , list, res):
        if k ==0:
            res.append(list)
            return
        for i in range(index,len(nums)):
            self.dfs(nums,k-1,i+1,list+[nums[i]],res)
            
            
        
# @lc code=end

