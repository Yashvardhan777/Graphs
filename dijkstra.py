class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0
        q = [[S, 0]]
        while len(q):
            x, wX = q.pop(0)
            
            for v, wV in adj[x]:
                if dist[v] > (wX + wV):
                    dist[v] = wX + wV
                    q.append([v, dist[v]])
                    
                    
        return dist
