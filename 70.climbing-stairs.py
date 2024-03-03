#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,2]
        for i in range(2,n):
            arr.append(arr[i-1]+arr[i-2])
        return arr[n-1]
# @lc code=end

