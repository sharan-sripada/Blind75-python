#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes=[]
        ans=float('inf')
        for time in timePoints:
            h,m=[int(s) for s in time.split(':')]
            minutes.append(h*60+m)
        minutes.sort()
        for i in range(len(minutes)-1):
            if minutes[i+1]-minutes[i]<ans:
                ans=minutes[i+1]-minutes[i]
            
        if len(minutes)>1 and 24*60-minutes[-1]+minutes[0] <ans:
            ans=24*60-minutes[-1]+minutes[0]
        return ans
            
            
        
# @lc code=end

