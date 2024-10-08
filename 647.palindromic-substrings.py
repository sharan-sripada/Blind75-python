#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        dp = [[False for _ in range(len(s))] for _ in range(len(s)) ]
        for i in range(len(s)):
            for j in range(i+1):
                if s[i]==s[j] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i]=True
                    ans+=1
        return ans
        
# @lc code=end

