#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        n= n//2 +1
        a,b = 0,0
        i,j = 0,0
        for k in range(n):
            if i >= len(nums1):
                a=b
                b = nums2[j]
                j+=1
            elif j >= len(nums2):
                a=b
                b = nums1[i]
                i+=1
            elif nums1[i]<=nums2[j]:
                a=b
                b=nums1[i]
                i+=1
            else:
                a=b
                b=nums2[j]
                j+=1
                
        if (len(nums1)+len(nums2))%2==0:
            return (a+b)/2 
        else: 
            return b/1
            
                
                
            
                
# @lc code=end

