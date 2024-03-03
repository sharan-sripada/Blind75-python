#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        i,j,carry = len(a)-1,len(b)-1,0
        while i>=0 or j>=0:
            sum =carry
            if i>=0:
                sum+=ord(a[i])-ord('0')
            if j>=0:
                sum+=ord(b[j])-ord('0')
            i,j =i-1,j-1
            carry = sum//2
            res+=str(sum%2)
        if carry >0:
            res+=str(carry)
        
        return res[::-1]

            
        
# @lc code=end

