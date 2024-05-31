#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def subsets(nums, index, XOR):
            if index == len(nums):
                return XOR
            withElement = subsets(nums, index+1, XOR^nums[index])
            withoutElement = subsets(nums, index+1, XOR)
            
            return withElement + withoutElement
        return subsets(nums,0,0)
            
# @lc code=end

