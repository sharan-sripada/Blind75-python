#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt= Counter(words[0])
        for w in words:
            curr_cnt= Counter(w)
            for i in cnt:
                cnt[i]=min(cnt[i],curr_cnt[i])
            
        ans=[]
        for i in cnt:
            for j in range(cnt[i]):
                ans.append(i)
        return ans
    
        
        
# @lc code=end

