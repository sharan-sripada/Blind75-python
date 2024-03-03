#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj = [ set() for _ in range(n)]
        for i,j in edges:
            adj[i].add(j)
            adj[j].add(i)
        
        leaves= [i for i in range(n) if len(adj[i])==1]
        
        while n >2:
            n-=len(leaves)
            newLeaves=[]
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j])==1:
                    newLeaves.append(j)
                
            leaves=newLeaves
        return leaves

                
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     visited = [False] * n
        
    #     res = 0
        
    #     adj = [[] for _ in range(n)]
        
    #     ans = [0 for _ in range(n)]
        
    #     roots=[]
        
    #     for edge in edges:
            
    #         adj[edge[0]].append(edge[1])
    #         adj[edge[1]].append(edge[0])
            
    #     # print(adj)
        
    #     for i in range(0,n):
    #         res = self.dfs(adj,visited,i,0)
    #         ans[i]=res
        
    #     # print(ans)
    #     print(min(ans))
    #     for i in range(0,n):
    #         if int(min(ans)) == ans[i]:
    #             roots.append(i)
    #     print(roots)
    
    #     return roots       
    # def dfs(self,adj,visited,current,len):
    #     m = len
    #     visited[current]= True
    #     for a in adj[current]:
    #         if visited[a]:
    #             continue
    #         visited[a]= True
    #         m = max(m, self.dfs(adj,visited,a,len+1))
    #         # print ( current, a)
    #         visited[a]= False
    #     visited[current]= False
    #     return m
    
         
            
        
# @lc code=end

