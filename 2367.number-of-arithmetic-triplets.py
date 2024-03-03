#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans =0
        n=len(nums)
        for i in range(n):
            j,k=i-1,i+1
            while j>=0 and k<n:
                if nums[i]-nums[j]==nums[k]-nums[i]==diff:
                    ans+=1
                    k+=1
                    j-=1
                    continue
                elif nums[i]-nums[j]<diff:
                    j-=1
                
                elif nums[k]-nums[i]<diff:
                    k+=1
                else:
                    break
        return ans
        
# @lc code=end

