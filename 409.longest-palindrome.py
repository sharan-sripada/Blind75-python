#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count={}
        oddFlag = False
        ans=0
        for c in s:
            count[c]= count.get(c, 0) + 1
        for v in count.values():
            if v%2==0:
                ans+=v
            else:
                ans+=(v-1)
                oddFlag=True
        if(oddFlag):
            ans+=1
        return ans

# @lc code=end

