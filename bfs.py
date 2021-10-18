class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q = [0]
        res = []
        visited = [0] * V
        while q:
            temp = q.pop(0)
            
            res.append(temp)
            for i in adj[temp]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1


        return res