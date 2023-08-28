#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map= {}

        for i,n in enumerate(nums):
            if n in map:
                return [i,map.get(n)]
            map[target-n]=i
        return
        
# @lc code=end

