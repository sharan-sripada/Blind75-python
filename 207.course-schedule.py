#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [0] * numCourses
        g = [[] for _ in range(numCourses)]

        for i,j in prerequisites:
            pre[i]+=1
            g[j].append(i)

        bfs = [ i for i in range(numCourses) if pre[i]==0]

        for i in bfs:
            for j in g[i]:
                pre[j]-=1
                if pre[j]==0:
                    bfs.append(j)

        return len(bfs) == numCourses



            

        
            
            
# @lc code=end

