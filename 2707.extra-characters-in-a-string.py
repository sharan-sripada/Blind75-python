#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#

# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words=set(dictionary)
        res=0
        
        dp={len(s):0}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            res=1+dfs(i+1)
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    res=min(res,dfs(j+1))
            dp[i]=res
            return res
        
        return dfs(0)
                    
            
            
        
# @lc code=end

