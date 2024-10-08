#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        x=0
        left=[]
        for a in arr:
            left.append(x)
            x^=a
        left.append(x)
        right=[0 for i in range(len(arr)+1)]
        a=0
        for i in range(len(arr)-1,-1,-1):
            a^=arr[i]
            right[i]=a
        ans=[]
        for query in queries:
            ans.append(x^left[query[0]]^right[query[1]+1])
        
        return ans
        
# @lc code=end

