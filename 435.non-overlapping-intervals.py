#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end=float('-inf')
        ans=0
        for s,e in sorted(intervals, key =lambda i: i[1]):
            if s>=end:
                end=e
            else:
                ans+=1
        return ans
        
# @lc code=end

