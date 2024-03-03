#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 1
        s=0
        for i in range(0,len(arr)-1):
            s+=(i+1)
            s-=(arr[i]+1)
            print(s)
            if s==0:
                chunks+=1
        return chunks
                
        
# @lc code=end

