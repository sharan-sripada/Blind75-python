#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxProfit = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                maxProfit= max(maxProfit, prices[r]-prices[l])
            else: 
                l=r
            r+=1
        return maxProfit

        
        
# @lc code=end

