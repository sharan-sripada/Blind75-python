#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(curr):
            if curr>n:
                return
            res.append(curr)
            curr=curr*10
            for i in range(10):
                dfs(curr+i)
        res=[]
        
        for i in range(1,10):
            dfs(i)
        return res
            
            
        
# @lc code=end

