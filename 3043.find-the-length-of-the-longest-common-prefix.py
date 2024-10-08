#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr2)>len(arr1):
             arr1,arr2=arr2,arr1
        ans=0
        prefix=set()
        for n in arr2:
            while n:
                prefix.add(n)
                n//=10
        
        for n in arr1:
            while n and n not in prefix:
                n//=10
            if n:
                ans=max(ans,len(str(n)))
        return ans
                
        
# @lc code=end

