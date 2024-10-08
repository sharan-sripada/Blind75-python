#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        dp =[0]*(len(s)+1)
        dp[0]=1
        dp[1]= 0 if s[0]=='0' else 1
        for i in range(1,len(s)):
            if s[i]!='0':
                dp[i+1]+=dp[i]
            
            if int(s[i-1:i+1])<=26 and int(s[i-1:i+1])>=10:
                # print(int(s[i-1:i+1]))
                dp[i+1]+=dp[i-1]
        # print(dp)
        return dp[len(s)]
            
        
        
        
# @lc code=end

