#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s={c for c in allowed}
        ans=len(words)
        for word in words:
            for c in word:
                if c not in s:
                    ans-=1
                    break
        return ans
# @lc code=end

