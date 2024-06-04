#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j=0,0
        m,n=len(s),len(t)
        while i<m and j<n:
            if s[i]==t[j]:
                j+=1
            i+=1
        return n-j
        
# @lc code=end

