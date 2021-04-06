class Solution:
    
    def __init__(self):   
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        
        self.graph[u].append(v)
        
    def BFS(self, s, grid, n, m):
        
        queue = []
        visited = [False] * (n * m)
        visited[s] = True
        queue.append(s)
        
        while(queue):
            a = queue.pop(0)
            
            for i in self.graph[a]:
                if(grid[i // m][i % m] == 1):
                    a1 = abs((i // m) - (s // m))
                    b1 = abs((i % m) - (s % m))
                    
                    return(a1+b1)
                if(visited[i] == False):
                    visited[i] = True
                    queue.append(i)
                    
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        s = Solution()
        n = len(grid)
        m = len(grid[0])
        check1 = False
        check2 = False
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 0):
                    check1 = True
                else:
                    check2 = True
                if(grid[i][j] == 0 or grid[i][j] == 1):
                    if(i != 0):
                        s.addEdge(i*m + j, (i-1)*m + j)
                    if(i != n-1):
                        s.addEdge(i*m + j, (i+1)*m + j)
                    if(j != 0):
                        s.addEdge(i*m + j, i*m + (j-1))
                    if(j != m-1):
                        s.addEdge(i*m + j, i*m + (j+1))
        
        
        if(check1 == False or check2 == False):
            return -1
        ma = 0
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 0):
                    c = s.BFS(i*m + j, grid, n ,m)
                    if(c > ma):
                        ma = c
        return ma                
