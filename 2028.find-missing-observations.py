#
# @lc app=leetcode id=2028 lang=python3
#
# [2028] Find Missing Observations
#

# @lc code=start
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        x = mean*(n+len(rolls))-sum(rolls)
        ans=[]
        if n*6<x or n*1>x:
            return []
        print(x)
        while x>0 and n>0:
            ans.append(x//n)
            x-=x//n
            n-=1
            
        return ans
# @lc code=end

