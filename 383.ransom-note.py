#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineSet= set(magazine)
        for c in ransomNote:
            if c not in magazineSet:
                return False
        return True

        
# @lc code=end

