#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        ans=0
        soFar=0
        for i in nums:
            if i==m:
                soFar += 1
            else:
                soFar=0
            ans=max(soFar,ans)
        return ans
        
# @lc code=end

