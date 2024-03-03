#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =1
        number = nums[0]
        for i in range(1,len(nums)):
            if(count ==0):
                number = nums[i]
            count+=1 if number==nums[i] else -1
        return number
        
# @lc code=end

