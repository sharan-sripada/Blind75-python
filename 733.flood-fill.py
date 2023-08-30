#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rlen, clen, scolor = len(image), len(image[0]),image[sr][sc]
        def dfs(r,c):
            if (not(0<=r<rlen and 0<=c<clen)) or image[r][c]!=scolor:
                return
            image[r][c]=color
            
            for (x,y) in ((-1,0),(0,-1),(1,0),(0,1)):
                dfs(r+x,c+y) 
        if scolor!=color:
            dfs(sr,sc)
        return image
# @lc code=end

