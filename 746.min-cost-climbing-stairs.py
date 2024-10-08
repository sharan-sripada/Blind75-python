#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr=[cost[0],cost[1]]
        l = len(cost)
        if l<2:
            return 0
        for i in range(2,l,1):
            arr.append(min(arr[i-1],arr[i-2])+cost[i])
        return min(arr[l-2],arr[l-1])
        
        
# @lc code=end

