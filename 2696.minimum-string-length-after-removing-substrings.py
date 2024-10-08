#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        stack=[]
        for letter in s:
            if letter == 'B':
                if stack[-1]=='A':
                    stack.pop()
                else:
                    stack.append(letter)
                
            elif letter == 'D':
                if stack[-1]=='C':
                    stack.pop()
                else:
                    stack.append(letter)
            else:
                stack.append(letter)
        return len(stack)
        
# @lc code=end

