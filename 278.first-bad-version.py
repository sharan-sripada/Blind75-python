#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r=1,n
        while l<r:
            mid=l+(r-l)//2
            if isBadVersion(mid):
                r=mid
            else:
                l=mid
        return l
        
# @lc code=end

