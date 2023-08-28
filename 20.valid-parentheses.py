#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = { ")":"(", "}":"{", "]":"["}
        for c in s:
            if c in closeOpen:
                if stack and stack[-1]== closeOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True
# @lc code=end

