#
# @lc app=leetcode id=2220 lang=python3
#
# [2220] Minimum Bit Flips to Convert Number
#

# @lc code=start
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x=start^goal
        ans=0
        while x!=0:
            if x&1:
                ans+=1
            x=x>>1
        return ans
        
# @lc code=end

