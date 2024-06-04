#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in nums:
            xor= xor^i
        bit=1
        while not(bit & xor):
            bit = bit <<1
        x,y =0,0
        for i in nums:
            if i&bit:
                x=x^i
            else:
                y=y^i
        return [x,y]
        
# @lc code=end

