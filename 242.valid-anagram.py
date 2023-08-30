#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        for c in s:
            if c in map:
                map[c]+=1
            else:
                map[c]=1
        for c in t:
            if c in map:
                map[c]-=1
            else:
                return False
            if map[c]==0:
                map.pop(c,None)
        return len(s)==len(t)
# @lc code=end

