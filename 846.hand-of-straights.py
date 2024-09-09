#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        for i in sorted(c):
            if c[i]>0:
                for j in range(groupSize-1,-1,-1):
                    c[i+j]-=c[i]
                    if c[i+j]<0:
                        return False
        return True
        
# @lc code=end

