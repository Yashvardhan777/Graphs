class Solution:
    
    #Function to return list containing vertices in Topological order.
    def dfs(self, V, adj, visited, stack):
        
        visited[V] = True
        for v in adj[V]:
            if visited[v] == False:
                self.dfs(v, adj, visited, stack)
                
        stack.append(V)
        
    def topoSort(self, V, adj):
        # Code here
        visited = [False] * V
        stack = []
        
        for i in range(V):
            if visited[i] == False:
                self.dfs(i, adj, visited, stack)
                
                
        return stack[::-1]
        