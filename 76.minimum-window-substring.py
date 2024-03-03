#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r,start,end=0,0,0,0
        m = defaultdict(int)
        for c in t:
            m[c]+=1
        cnt = len(t)
        while(r<len(s)):
            if m[s[r]] >0:
                cnt-=1
            m[s[r]]-=1
            r+=1
            while cnt==0:
                print(l,r)
                if end ==0:
                    end = r
                if end-start > r-l:
                    start = l
                    end =r
                m[s[l]]+=1
                if m[s[l]]>0:
                    cnt+=1
                l+=1
            
            
        return s[start:end]
                    
                    

# @lc code=end

