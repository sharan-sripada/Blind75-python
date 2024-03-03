#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        endWord =[False]*len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (endWord[i-len(w)] or i-len(w)==-1 ):
                    endWord[i] = True
        return endWord[-1]
            
            
        
        
# @lc code=end

