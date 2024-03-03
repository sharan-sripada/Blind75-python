#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        self.dfs(candidates, target, res, [], 0)
        return res
        
    def dfs(self, candidates, target, res, list , index):
        if target < 0:
            return
        if target == 0:
            res.append(list)
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue           
            self.dfs(candidates, target- candidates[i], res,list+[candidates[i]],i+1)
            
# @lc code=end

