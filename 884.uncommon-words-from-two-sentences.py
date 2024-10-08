#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        all_words=s1.split()+s2.split()
        word_count=Counter(all_words)
        return [ word for word in word_count if word_count[word]==1]
# @lc code=end

