class Solution:
    
    #Function to detect cycle in an undirected graph.
    def solve(self, V, adj, visited, parent):
        visited[V] = True
        
        for v in adj[V]:
            if visited[v] == False:
                if self.solve(v, adj, visited, V):
                    return True
                    
            elif parent != v:
                return True
                
        
        return False
        
    def isCycle(self, V, adj):
        #Code here
        visited = [False] * V
        
        for i in range(V):
            if visited[i] == False:
                if self.solve(i, adj, visited, -1):
                    #  print(i)
                    return True
                    
                    
        return False