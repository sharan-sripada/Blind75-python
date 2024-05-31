#
# @lc app=leetcode id=2597 lang=python3
#
# [2597] The Number of Beautiful Subsets
#

# @lc code=start
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        global res
        res = -1
        list= []
        def backtrack(nums, index, k, list ):

            global res
            res = res +1
            # print(index)
            # print(list)
            
            for i in range(index, len(nums)):
                if nums[i] - k not in list :
                    backtrack(nums, i+1, k,list+[nums[i]])
                
        backtrack(nums,0,k,[])
        return res     
        
# @lc code=end

