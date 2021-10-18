class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def solve(self, V, visited, adj, res):
        if visited[V]:
            return 
        
        visited[V] = 1
        res.append(V)
        for v in adj[V]:
            self.solve(v, visited, adj, res)
        
        
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [0] * V
        res = []
        for i in range(V):
            if visited[i] == 0:
                self.solve(i, visited, adj, res)
                
        return res