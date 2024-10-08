#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=1:
            return s
        maxLen=1
        maxStr=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i]=True
            for j in range(i+1):
                if s[i]==s[j] and (i-j<=2 or dp[j+1][i-1]):
                    dp[j][i]=True
                    if i-j+1>maxLen:
                        maxLen=i-j+1
                        maxStr=s[j:i+1]
        return maxStr
        
        
        
# @lc code=end

