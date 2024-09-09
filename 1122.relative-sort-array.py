#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0]*1001
        for i in arr1:
            count[i]+=1
        ans=[]
        for j in arr2:
            while count[j]>0:
                count[j]-=1
                ans.append(j)
        for i in range(1001):
            while count[i]>0:
                ans.append(i)
                count[i]-=1
        return ans
                        
        
# @lc code=end

