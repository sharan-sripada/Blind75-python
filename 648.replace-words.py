#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s = sentence.split(' ')
        ans=[]
        for word in s:
            add = False
            for i in range(len(word)):
                if word[0:i] in dictionary:
                    ans.append(word[0:i])
                    add = True
                    break
                
            if add == False:
                ans.append(word)
                
        return " ".join(ans)
                    
        
# @lc code=end

