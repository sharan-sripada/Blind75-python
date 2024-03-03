#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)< len(p):
            return []
        i,j = 0, len(p)-1
        res = []
        
        w1 = defaultdict(int)
        w2 = defaultdict(int)
        for k in range(0,j+1):
            w1[s[k]]= w1.get(s[k],0) +1
            w2[p[k]] = w2.get(p[k],0) +1  
        if w1 ==w2:
            res.append(i)
        
        # print(j, len(s))
        while j < len(s)-1:
            j+=1

            w1[s[i]]-=1
            if w1[s[i]]==0 :
                del w1[s[i]]
            
            w1[s[j]]=w1.get(s[j],0)+1
            
            # print(w1,w2)
            
            i+=1
            
            if w1 ==w2:
                res.append(i)
        return res
                
                  
            
        
# @lc code=end

