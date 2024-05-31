 #
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#

# @lc code=start
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans=0
        n=len(arr)
        for i in range(n-1):
            xor=arr[i]
            for j in range(i+1,n):
                xor^=arr[j]
                if xor == 0:
                    ans=ans+(j-i)
        return ans
            
        
# @lc code=end

