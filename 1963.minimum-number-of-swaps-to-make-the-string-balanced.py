#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        open_bracket = 0
        for c in s:
            if open_bracket > 0 and c == ']':
                open_bracket -= 1
            elif c == '[':
                open_bracket += 1
        return (open_bracket + 1) // 2
        
# @lc code=end

