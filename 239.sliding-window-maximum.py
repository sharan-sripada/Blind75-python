#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i,j=0,k-1
        s=sum(nums[0:k])
        m=s
        while j<len(nums)-1:
            i+=1
            j+=1
            s=s-nums[i]+nums[j]
            m=max(s,m)
        return m
        
            
            
            
# @lc code=end

