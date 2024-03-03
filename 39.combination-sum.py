#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
            self.dfs(candidates, target- candidates[i], res,list+[candidates[i]],i)
            
# @lc code=end

