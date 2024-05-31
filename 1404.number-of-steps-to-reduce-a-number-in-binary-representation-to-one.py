#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        n=len(s)-1
        ans=0
        s=list(s)
        while n>0:
            # print(s)
            # print(n)
            if s[n]=='0':
                n=n-1
            else:
                m=n
                while m>=0 and s[m]!='0':
                    s[m]='0'
                    m=m-1
                if m>=0 and s[m]=='0':
                    s[m]='1'
                else:
                    s=[1]+s
            ans=ans+1
        if s[n]!='1':
            ans=ans+1
        return ans
                
            
# @lc code=end

