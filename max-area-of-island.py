class Solution:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def BFS(self, s, grid, visited):
        queue = []
        c = 1
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop(0)

            for i in self.graph[s]:
                if (visited[i] == False):
                    queue.append(i)
                    visited[i] = True
                    c = c + 1
        return (c, visited)            
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        s = Solution()
        visited = [False] * (n*m)
        for i in range(n):
            for j in range(m):
                if(i != 0 and grid[i][j] == 1 and grid[i-1][j] == 1):
                    s.addEdge(i*m + j, (i-1)*m + j)
                if(i != n-1 and grid[i][j] == 1 and grid[i+1][j] == 1):
                    s.addEdge(i*m + j, (i+1)*m + j)
                if(j != 0 and grid[i][j] == 1 and grid[i][j-1] == 1):
                    s.addEdge(i*m + j, i*m + (j-1))
                if(j != m-1 and grid[i][j] == 1 and grid[i][j+1] == 1):
                    s.addEdge(i*m + j, i*m + (j+1))
                    
        ma = 0
        for i in range(n):
            for j in range(m):
                if(visited[i*m + j] == False and grid[i][j] == 1):
                    c, visited = s.BFS(i*m + j, grid, visited)
                    if(c > ma):
                        ma = c
        return ma
