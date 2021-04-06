class Solution:
    
    def __init__(self):
        self.graph = defaultdict(list)
        self.size = 400
        
    def addEdge(self,u,v):
        #print(list(self.graph.keys()))
        self.graph[u].append(v)
    
    def removeEdge(self, u, v):
        
        try:
            self.graph[u].remove(v)
            self.graph[v].remove(u)
        except:
            #print("already deleted")
            pass

        
    def BFS(self, s, t):
        #print(self.graph.values())
        visited = [False] * (self.size*self.size)
        queue = []
        queue.append(s)
        
        while(queue):
            a = queue.pop(0)
            for i in self.graph[a]:
                if(i == t):
                    return True
                if(visited[i] == False):
                    queue.append(i)
                    visited[i] = True
        return False            
            
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        s = Solution()
        if(blocked == []):
            return True
       # if(source == [0,999997]):
        #    return False
        source[0] = source[0]%self.size
        source[1] = source[1]%self.size
        target[0] = target[0]%self.size
        target[1] = target[1]%self.size
        
        #print(source)
        #print(target)
        for i in blocked:
            i[0] = i[0]%self.size
            i[1] = i[1]%self.size
        #print(blocked)
        for i in range(self.size):
            for j in range(self.size):
                if(i != 0):
                    s.addEdge(i*self.size + j, (i-1)*self.size + j)
                if(i != self.size - 1):
                    s.addEdge(i*self.size + j, (i+1)*self.size + j)
                if(j != 0):
                    s.addEdge(i*self.size + j, i*self.size + (j-1))
                if(j != self.size - 1):
                    s.addEdge(i*self.size + j, i*self.size + (j+1))
        for i in blocked:
            if(i[0]*self.size + i[1] == source[0]*self.size + source[1]):
                return False
            if(i[0]*self.size + i[1] == target[0]*self.size + target[1]):
                return False
            if(i[0] != 0):
                s.removeEdge(i[0]*self.size + i[1] , (i[0]-1)*self.size + i[1])
            if(i[0] != self.size - 1):
                s.removeEdge(i[0]*self.size + i[1] , (i[0]+1)*self.size + i[1])
            if(i[1] != 0):
                s.removeEdge(i[0]*self.size + i[1] , i[0]*self.size + i[1]-1)
            if(i[0] != self.size - 1):
                s.removeEdge(i[0]*self.size + i[1] , i[0]*self.size + i[1]+1)
    
        
        source1 = (source[0])*self.size + (source[1])
        target1 = (target[0])*self.size + (target[1])
        #print(self.graph)
        return(s.BFS(source1, target1))
        
        
