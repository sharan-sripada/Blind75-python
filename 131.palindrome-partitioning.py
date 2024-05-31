#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr=[]
        self.subset(res,0,s,curr)
        return res
    
    def subset(self,res,index,s,curr):
        if len(s)==index:
            res.append(curr.copy())
        for i in range(index,len(s),1):
            if self.palindrome(s,index,i):
                curr.append(s[index:i+1])
                self.subset(res,i+1,s,curr)
                curr.pop()
            
    
    
    def palindrome(self,s,i,j):
        while i < j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
            
                   
        
# @lc code=end

