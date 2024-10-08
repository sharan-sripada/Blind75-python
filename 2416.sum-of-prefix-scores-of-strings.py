#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#

# @lc code=start
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        m = deafultdict(0)
        for word in words:
            for i in range(1,len(word)):
                m[word[0:i]]+=1
                
        ans=[]
        for word in words:
            temp=0
            for i in range(1,len(word)):
                temp+=m[word[0:i]]
            ans.append(temp)
        return ans
        
        
        
# @lc code=end

