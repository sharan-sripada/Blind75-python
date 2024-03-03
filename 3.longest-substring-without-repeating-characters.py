#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r =0,0
        set=[]
        length=0

        while(r<len(s)):
            if(s[r] in set):
                while(s[r] in set):
                    set.remove(s[l])
                    l=l+1
                set.append(s[r])
                r=r+1
            else:
                set.append(s[r])
                r=r+1
            length=max(length,r-l)
        return length


        
# @lc code=end

