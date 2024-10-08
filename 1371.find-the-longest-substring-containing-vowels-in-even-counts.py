#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#

# @lc code=start
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask=0
        ans=0
        m={0:-1}
        vowels='aeiou'
        
        for i,c in enumerate(s):
            if c in vowels:
                
                mask^=(ord(c)-ord('a')+1)
            
            if mask in m:
                ans=max(ans,i-m[mask])
            else:
                m[mask]=i
            
        return ans
        
        
# @lc code=end

