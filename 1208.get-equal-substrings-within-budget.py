#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [-1]*len(s)
        for i in range(0,len(s)):
            diff[i]=abs(ord(s[i])-ord(t[i]))
        ans,rdiff=0,0
        i,j=0,0
        while j<len(s):
            while rdiff+diff[j]>maxCost and i<j:
                rdiff=rdiff-diff[i]
                i=i+1
            
            while j<len(s) and rdiff+diff[j]<=maxCost :
                rdiff=rdiff+diff[j]
                ans=max(ans,j-i+1)
                j=j+1
            if i==j:
                i=i+1
                j=j+1
            
        return ans
            
        
        
# @lc code=end

